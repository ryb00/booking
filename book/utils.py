from datetime import timedelta, datetime, date

from book.models import Schedule, Number_of_tables_to_order


def get_end_time(start_time, duration_hours):
    return (datetime.combine(date(1, 1, 1), start_time) + timedelta(hours=duration_hours)).time()


AVAILABLE_TABLES = 10


def check_available_tables_for_time(date_of_visit, start_time, duration_hours, number_of_visitors):
    end_time = get_end_time(start_time, duration_hours)

    existing_bookings = Schedule.objects.filter(
        date_of_visit=date_of_visit,
        time_of_visit__lte=end_time,
        time_of_visit__gte=start_time
    )

    booked_tables_count = 0
    for booking in existing_bookings:
        booked_tables_count += calculate_tables_needed(booking.number_of_visitors)

    need_tables_count = calculate_tables_needed(number_of_visitors)

    available_tables = AVAILABLE_TABLES - booked_tables_count

    if ((available_tables < need_tables_count) or (date_of_visit < date.today())):
        return False, "Sorry, not enough tables available"
    else:
        return True, f"{available_tables} tables available."


def calculate_tables_needed(number_of_visitors):
    visitors_tables = {record.visitor_number: record.table_number for record in Number_of_tables_to_order.objects.all()}

    if number_of_visitors in visitors_tables:
        return visitors_tables[number_of_visitors]

    sorted_keys = sorted(visitors_tables.keys())
    total_tables_needed = 0
    remaining_visitors = number_of_visitors

    for key in reversed(sorted_keys):
        while remaining_visitors >= key:
            total_tables_needed += visitors_tables[key]
            remaining_visitors -= key
            if remaining_visitors == 0:
                return total_tables_needed

    if remaining_visitors > 0:
        for key in sorted_keys:
            if key >= remaining_visitors:
                total_tables_needed += visitors_tables[key]
                break
        else:
            total_tables_needed += (remaining_visitors // sorted_keys[-1] + (
                1 if remaining_visitors % sorted_keys[-1] > 0 else 0)) * visitors_tables[sorted_keys[-1]]

    return total_tables_needed
