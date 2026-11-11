
#!/usr/bin/python3
"""Generate personalized invitations from a text template."""


def generate_invitations(template, attendees):
    """Create one invitation file for each attendee."""

    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list.")
        return

    if not all(isinstance(item, dict) for item in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = (
        "name",
        "event_title",
        "event_date",
        "event_location"
    )

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + key + "}", str(value)
            )

        filename = "output_{}.txt".format(index)

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(invitation)
        except OSError as error:
            print("Error writing {}: {}".format(filename, error))
