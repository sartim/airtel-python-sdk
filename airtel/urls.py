URL = {}

# Sandbox Urls
URL["sandbox"] = {}
URL["sandbox"]["v1"] = {}
URL["sandbox"]["v1"]["activate_subscription"] = "https://{ip}:{port}/smartapi/services/subscription/v1/activation"\
    .format(ip="sandbox", port=8000)
URL["sandbox"]["v1"]["deactivate_subscription"] = "https://{ip}:{port}/smartapi/services/subscription/v1/deactivation"\
    .format(ip="sandbox", port=8000)

# Prod Urls
URL["production"] = {}
URL["production"]["v1"] = {}
URL["production"]["v1"]["activate_subscription"] = "https://{ip}:{port}/smartapi/services/subscription/v1/activation"\
    .format(ip="production", port=8000)
URL["production"]["v1"]["deactivate_subscription"] = "https://{ip}:{port}/smartapi/services/subscription/v1/deactivation"\
    .format(ip="sandbox", port=8000)
