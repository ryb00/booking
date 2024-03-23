# RESTAURANT FOODIE

This site is a restaurant reservation system.

## Site design

! (/book/static/images/laptop.png)

# Features

## List of reservations

The site contains a list of the user's bookings.

! (/book/static/images/your_booking.png)

The user can delete his booking. A message is displayed to the user:

! (/book/static/images/delete.png)

## Booking

The user can book a table by specifying the date, time, number of people and number of hours:

! (/book/static/images/booking.png)

If there is no free table at the specified time and date, the user sees a message about this:

! (/book/static/images/sorry.png)

If there is a free table, the reservation information is added to the reservation list.

## Principle of booking accounting

This accounting system contains 2 tables: Number_of_tables_to_order and Schedule.

The Number_of_tables_to_order table contains two attributes:
visitor_number (IntegerField, unique),
table_number (IntegerField). 

This table is filled out in the site admin panel by a restaurant employee. It indicates how many tables are needed for a group of guests.  If the order is for 4 people, then 1 table is enough for them, if the order is for 5 people, then 2 tables are needed.

The Schedule table contains five attributes:
date_of_visit (DateField),
time_of_visit (TimeField),
number_of_visitors (IntegerField),
number_of_hours (IntegerField),
visitor (ForeignKey, User).

When making a reservation, data is first taken from the Number_of_tables_to_order table about how many tables are needed for the specified number of guests. Then the data on how many tables are already reserved for the specified time and date is taken from the Schedule table and the required number of tables is added to it. This number is compared with the total number of tables, which is specified by the AVAILABLE_TABLES constant and in this case is 10.

# Testing

The site was tested in the Chrome browser. No errors found.

# Deployment

The site was deployed to Heroku page.
Link  https://booktable-25845d9db893.herokuapp.com/
Superuser: login admin, password 12345678
Github: https://ryb00.github.io/booking/

# Credits

The icons in the footer were taken from https://fontawesome.com/
The favicon was taken from https://favicon.io/
The images were taken from https://www.pexels.com/ and https://pixabay.com/
Information when writing the code was taken from https://www.w3schools.com/, youtube.
The website developed as part of the first assignment of this course was used.
