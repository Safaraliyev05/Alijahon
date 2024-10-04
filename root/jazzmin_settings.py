JAZZMIN_SETTINGS = {
    "site_title": "Alijahon",
    "site_header": "Alijahon",
    "site_brand": "Sardor admin",
    # "site_logo": "apps/assets/img/icons/spot-illustrations/alijahon.jpg",

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    "custom_links": {
        "products": [
            {
                "name": "Products",
                # "models": [
                #     "apps.ProductProxy",
                #     "apps.CategoryProxy",
                # ],
                "icon": "fas fa-box",
            },
        ],
    },
    "icons": {
        "apps.ProductProxy": "fas fa-box",
        "apps.CategoryProxy": "fas fa-list",
        "apps.Favourite": "fas fa-heart",
        "apps.OrderProxy": "fas fa-shopping-cart",
        "apps.NewOrderProxy": "fas fa-plus-circle",
        "apps.ReadyOrderProxy": "fas fa-check-circle",
        "apps.DeliverOrderProxy": "fas fa-truck",
        "apps.CantPhoneOrderProxy": "fas fa-phone-alt",
        "apps.CanceledOrderProxy": "fas fa-times-circle",
        "apps.ReturnedOrderProxy": "fas fa-undo",
        "apps.ArchivedOrderProxy": "fas fa-archive",
        "apps.HoldOrderProxy": "fas fa-pause-circle",
        "apps.Stream": "fas fa-video",
        "apps.Competition": "fas fa-trophy",
        "apps.DriverUserProxy": "fas fa-user-tie",
        "apps.OperatorUserProxy": "fas fa-user-cog",
        "apps.ManagerUserProxy": "fas fa-user-shield",
        "apps.UserProxy": "fas fa-user",
        "apps.AdminUserProxy": "fas fa-user-secret",
    },
    # "hide_apps": ["apps"],
}
