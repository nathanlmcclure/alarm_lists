# alarm_lists
# location_transfers

A former employer used a vendor's website to track the location and performance of their rental units.  Given that it was used to monitor performance, it could also send alerts when performance was outside of normal parameters.

The alert parameters were established along with a list of applicable units and parties to be contacted when the alarm was tripped.  Because we had teams in different regions, it became necessary to have separate alert lists for units in each region. That allowed each team to be notified only when one of their units triggered an alarm.

Although this vendor offered API endpoints, none of them were applicable for this purpose.  I wrote this code to give me a list of unit numbers on each alarm list.  I could then use that to verify that the unit was assigned properly by comparing it to the unit's assignment in our billing software (see link to the "location_transfers" repository for more info).

This script isn't complete, as it doesn't import the info from the billing software.  However, the extraction would be similar to the methods used in my location_transfers script.
