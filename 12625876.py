import math
import os
import sys
import warnings
import openpyxl

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

default_filename = "12625876.xlsx"

if os.path.exists(default_filename):
    filename = default_filename
elif os.path.exists("python excelsheet 12625876.xlsx"):
    filename = "python excelsheet 12625876.xlsx"
elif os.path.exists(os.path.join("data", "12625876.xlsx")):
    filename = os.path.join("data", "12625876.xlsx")
else:
    filename = default_filename

sheet_name = "Daily Log"
expected_days_count = 44

output_dir = "output"
output_filename = "12625876_python_output.txt"

# Excel column mapping (1-indexed)
col_date = 1
col_sleep = 2
col_fitness = 3
col_study = 4
col_coding = 5
col_class = 6
col_classes_attended = 7
col_other_activities = 8
col_total_tracked = 9
col_free_unaccounted = 10
col_day_feeling = 11
col_satisfaction_level = 12
col_energy_level = 13
col_notes = 14

feeling_score_map = {
    "Excellent": 5,
    "Good": 4,
    "Okay": 3,
    "Low": 2,
    "Very Low": 1,
}

satisfaction_score_map = {
    "Very Satisfied": 5,
    "Satisfied": 4,
    "Neutral": 3,
    "Dissatisfied": 2,
    "Very Dissatisfied": 1,
}

energy_score_map = {
    "High": 3,
    "Medium": 2,
    "Low": 1,
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for stream in self.streams:
            stream.write(data)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def read_column(filename, sheet_name, column, start_row=6):
    column_values = []
    try:
        workbook = openpyxl.load_workbook(filename, data_only=True)
        if sheet_name not in workbook.sheetnames:
            raise KeyError(f"Worksheet '{sheet_name}' was not found in {filename}")
        worksheet = workbook[sheet_name]

        for current_row in range(start_row, worksheet.max_row + 1):
            cell_value = worksheet.cell(row=current_row, column=column).value
            if cell_value is not None and cell_value != "":
                column_values.append(cell_value)

    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
    except KeyError as error_message:
        print(f"Error: {error_message}")
    except Exception as unexpected_error:
        print(f"Error reading column {column}: {unexpected_error}")

    return column_values


def valid_day_count(values_list):
    return len(values_list)


def compute_average(values_list):
    if not values_list:
        return 0.0

    accumulated_sum = 0.0
    valid_items_count = 0

    for current_value in values_list:
        if current_value is not None:
            try:
                accumulated_sum += float(current_value)
                valid_items_count += 1
            except (ValueError, TypeError):
                continue

    if valid_items_count == 0:
        return 0.0

    return accumulated_sum / valid_items_count


def tpi(filename, sheet_name):
    coding_minutes_list = read_column(filename, sheet_name, col_coding)
    return compute_average(coding_minutes_list)


def aai(filename, sheet_name):
    study_minutes_list = read_column(filename, sheet_name, col_study)
    class_minutes_list = read_column(filename, sheet_name, col_class)

    paired_day_count = min(len(study_minutes_list), len(class_minutes_list))
    if paired_day_count == 0:
        return 0.0

    daily_academic_minutes = [
        float(study_minutes_list[day_index]) + float(class_minutes_list[day_index])
        for day_index in range(paired_day_count)
    ]
    return compute_average(daily_academic_minutes)


def phai(filename, sheet_name):
    fitness_minutes_list = read_column(filename, sheet_name, col_fitness)
    return compute_average(fitness_minutes_list)


def sri(filename, sheet_name):
    sleep_minutes_list = read_column(filename, sheet_name, col_sleep)
    return compute_average(sleep_minutes_list)


def abi(filename, sheet_name):
    free_minutes_list = read_column(filename, sheet_name, col_free_unaccounted)
    return compute_average(free_minutes_list)


def tui(filename, sheet_name):
    total_tracked_list = read_column(filename, sheet_name, col_total_tracked)
    return compute_average(total_tracked_list)


def ei(filename, sheet_name):
    feeling_labels = read_column(filename, sheet_name, col_day_feeling)
    satisfaction_labels = read_column(filename, sheet_name, col_satisfaction_level)
    energy_labels = read_column(filename, sheet_name, col_energy_level)

    common_days = min(len(feeling_labels), len(satisfaction_labels), len(energy_labels))
    if common_days == 0:
        return 0.0

    cumulative_score = 0.0
    for day_index in range(common_days):
        feeling_text = str(feeling_labels[day_index]).strip()
        satisfaction_text = str(satisfaction_labels[day_index]).strip()
        energy_text = str(energy_labels[day_index]).strip()

        feeling_score = feeling_score_map.get(feeling_text, 3)
        satisfaction_score = satisfaction_score_map.get(satisfaction_text, 3)
        energy_score = energy_score_map.get(energy_text, 2)

        cumulative_score += (feeling_score + satisfaction_score + energy_score)

    return cumulative_score / (3.0 * common_days)


def dci(filename, sheet_name, expected_days=44):
    date_records = read_column(filename, sheet_name, col_date)
    logged_days = valid_day_count(date_records)

    if expected_days <= 0:
        return 0.0

    return (logged_days / float(expected_days)) * 100.0


def pai(tpi_s, aai_s, phai_s, sri_s, tui_s, ei_s, dci_val):
    return (
        0.15 * tpi_s
        + 0.20 * aai_s
        + 0.15 * phai_s
        + 0.20 * sri_s
        + 0.15 * tui_s
        + 0.10 * ei_s
        + 0.05 * dci_val
    )


def compute_pearson_r(list_a, list_b):
    paired_count = min(len(list_a), len(list_b))
    if paired_count < 2:
        return 0.0

    values_x = [float(item) for item in list_a[:paired_count]]
    values_y = [float(item) for item in list_b[:paired_count]]

    mean_x = compute_average(values_x)
    mean_y = compute_average(values_y)

    covariance_sum = 0.0
    variance_x_sum = 0.0
    variance_y_sum = 0.0

    for day_index in range(paired_count):
        difference_x = values_x[day_index] - mean_x
        difference_y = values_y[day_index] - mean_y
        covariance_sum += difference_x * difference_y
        variance_x_sum += difference_x * difference_x
        variance_y_sum += difference_y * difference_y

    denominator = math.sqrt(variance_x_sum * variance_y_sum)
    if denominator == 0.0:
        return 0.0

    return covariance_sum / denominator


def find_correlation_note(list_a, list_b, label_a, label_b):
    correlation_value = compute_pearson_r(list_a, list_b)

    if abs(correlation_value) >= 0.7:
        strength_description = "strong"
    elif abs(correlation_value) >= 0.3:
        strength_description = "moderate"
    elif abs(correlation_value) >= 0.1:
        strength_description = "weak"
    else:
        strength_description = "negligible"

    if correlation_value > 0:
        direction_description = "positive"
    elif correlation_value < 0:
        direction_description = "negative"
    else:
        direction_description = "neutral"

    summary_note = (
        f"r = {correlation_value:+.4f} "
        f"({strength_description} {direction_description} relationship between {label_a} and {label_b})"
    )
    return correlation_value, summary_note


def run_report():
    print("=" * 78)
    print("   Personal Activity Intelligence Report")
    print("=" * 78)
    print("Student Name     : Nitish Kapoor")
    print("Registration No. : 12625876")
    print("Course / Section : MCA (P164-NN1) / Section D1P2633")
    print(f"Data File        : {filename}")
    print(f"Worksheet        : {sheet_name}")
    print("-" * 78)

    dates_recorded = read_column(filename, sheet_name, col_date)
    logged_days_count = valid_day_count(dates_recorded)

    if logged_days_count == 0:
        print("Error: No data rows found in worksheet. Please check file path.")
        return

    first_logged_date = str(dates_recorded[0]).split()[0]
    last_logged_date = str(dates_recorded[-1]).split()[0]
    missing_days_count = max(0, expected_days_count - logged_days_count)

    print(f"Recording Period : {first_logged_date} to {last_logged_date}")
    print(f"Logged Days      : {logged_days_count} / {expected_days_count} expected days")
    print("-" * 78)

    sleep_list = read_column(filename, sheet_name, col_sleep)
    fitness_list = read_column(filename, sheet_name, col_fitness)
    study_list = read_column(filename, sheet_name, col_study)
    coding_list = read_column(filename, sheet_name, col_coding)
    class_list = read_column(filename, sheet_name, col_class)
    other_list = read_column(filename, sheet_name, col_other_activities)
    free_list = read_column(filename, sheet_name, col_free_unaccounted)

    feeling_labels = read_column(filename, sheet_name, col_day_feeling)
    satisfaction_labels = read_column(filename, sheet_name, col_satisfaction_level)
    energy_labels = read_column(filename, sheet_name, col_energy_level)

    feeling_nums = [feeling_score_map.get(str(x).strip(), 3) for x in feeling_labels]
    satisfaction_nums = [satisfaction_score_map.get(str(x).strip(), 3) for x in satisfaction_labels]
    energy_nums = [energy_score_map.get(str(x).strip(), 2) for x in energy_labels]

    avg_sleep = compute_average(sleep_list)
    avg_fitness = compute_average(fitness_list)
    avg_study = compute_average(study_list)
    avg_coding = compute_average(coding_list)
    avg_class = compute_average(class_list)
    avg_other = compute_average(other_list)
    avg_free = compute_average(free_list)

    print("\n1. Activity Data Summary (Daily Averages)")
    print("-" * 78)
    print(f"Expected number of days           : {expected_days_count}")
    print(f"Valid days recorded               : {logged_days_count}")
    print(f"Missing days                      : {missing_days_count}")
    print(f"Invalid / excluded records        : 0")
    print(f"Average Sleep / day               : {avg_sleep:.2f} min/day (~{avg_sleep / 60:.2f} hrs)")
    print(f"Average Fitness / day             : {avg_fitness:.2f} min/day (~{avg_fitness / 60:.2f} hrs)")
    print(f"Average Study / day               : {avg_study:.2f} min/day (~{avg_study / 60:.2f} hrs)")
    print(f"Average Coding / day              : {avg_coding:.2f} min/day (~{avg_coding / 60:.2f} hrs)")
    print(f"Average Class / day               : {avg_class:.2f} min/day (~{avg_class / 60:.2f} hrs)")
    print(f"Average Other Activities / day    : {avg_other:.2f} min/day (~{avg_other / 60:.2f} hrs)")
    print(f"Average Free / Unaccounted Time   : {avg_free:.2f} min/day (~{avg_free / 60:.2f} hrs)")
    print("-" * 78)

    tech_productivity_index = tpi(filename, sheet_name)
    academic_activity_index = aai(filename, sheet_name)
    physical_activity_index = phai(filename, sheet_name)
    sleep_recovery_index = sri(filename, sheet_name)
    activity_balance_index = abi(filename, sheet_name)
    time_utilization_index = tui(filename, sheet_name)
    experience_index = ei(filename, sheet_name)
    data_continuity_index = dci(filename, sheet_name, expected_days=expected_days_count)
    personal_activity_index = pai(
        tech_productivity_index,
        academic_activity_index,
        physical_activity_index,
        sleep_recovery_index,
        time_utilization_index,
        experience_index,
        data_continuity_index,
    )

    print("\n2. Activity Index Values")
    print("-" * 78)
    print(f"{'Index Name':<32} {'Acronym':<8} {'Value':<18} {'Unit / Scale'}")
    print("-" * 78)
    print(f"{'Tech Productivity':<32} {'TPI':<8} {tech_productivity_index:>10.2f}        min/day")
    print(f"{'Academic Activity':<32} {'AAI':<8} {academic_activity_index:>10.2f}        min/day")
    print(f"{'Physical Activity':<32} {'PhAI':<8} {physical_activity_index:>10.2f}        min/day")
    print(f"{'Sleep & Recovery':<32} {'SRI':<8} {sleep_recovery_index:>10.2f}        min/day")
    print(f"{'Activity Balance':<32} {'ABI':<8} {activity_balance_index:>10.2f}        min/day")
    print(f"{'Time Utilization':<32} {'TUI':<8} {time_utilization_index:>10.2f}        min/day")
    print(f"{'Experience Index':<32} {'EI':<8} {experience_index:>10.2f}        / 5")
    print(f"{'Data Continuity Index':<32} {'DCI':<8} {data_continuity_index:>10.2f}        %")
    print("-" * 78)
    print(f"{'Personal Activity Index':<32} {'PAI':<8} {personal_activity_index:>10.2f}        composite score")
    print("=" * 78)

    print("\n3. Key Correlation Findings")
    print("-" * 78)
    _, n1 = find_correlation_note(sleep_list, energy_nums, "Sleep Duration", "Energy Level")
    _, n2 = find_correlation_note(study_list, satisfaction_nums, "Study Time", "Satisfaction Level")
    _, n3 = find_correlation_note(coding_list, energy_nums, "Coding Time", "Energy Level")
    _, n4 = find_correlation_note(fitness_list, energy_nums, "Fitness Time", "Energy Level")
    _, n5 = find_correlation_note(class_list, free_list, "Class Time", "Free Time")

    print(f"1. Sleep <-> Energy         : {n1}")
    print(f"2. Study <-> Satisfaction   : {n2}")
    print(f"3. Coding <-> Energy        : {n3}")
    print(f"4. Fitness <-> Energy       : {n4}")
    print(f"5. Class <-> Free Time      : {n5}")
    print("=" * 78)


def main():
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)

    original_stdout = sys.stdout
    try:
        with open(output_path, "w", encoding="utf-8") as report_file:
            sys.stdout = Tee(original_stdout, report_file)
            run_report()
    finally:
        sys.stdout = original_stdout

    print(f"\nReport saved to: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    main()
