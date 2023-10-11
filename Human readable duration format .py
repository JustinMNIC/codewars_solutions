def format_duration(input):
    if input == 0:
        return "now"

    components = []

    years = input // 31_536_000
    if years > 0:
        components.append("{} year{}".format(years, 's' if years > 1 else ''))
        input %= 31_536_000

    days = input // 86_400
    if days > 0:
        components.append("{} day{}".format(days, 's' if days > 1 else ''))
        input %= 86_400

    hours = input // 3_600
    if hours > 0:
        components.append("{} hour{}".format(hours, 's' if hours > 1 else ''))
        input %= 3_600

    minutes = input // 60
    if minutes > 0:
        components.append("{} minute{}".format(minutes, 's' if minutes > 1 else ''))
        input %= 60

    seconds = input
    if seconds > 0:
        components.append("{} second{}".format(seconds, 's' if seconds > 1 else ''))

    if len(components) == 1:
        return components[0]
    elif len(components) == 2:
        return " and ".join(components)
    else:
        return ", ".join(components[:-1]) + " and " + components[-1]

print(format_duration(1))