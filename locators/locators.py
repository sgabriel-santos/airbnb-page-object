from selenium.webdriver.common.by import By


class HomeLocators():
    cookie_buttons = (By.CSS_SELECTOR, '[data-testid="main-cookies-banner-container"] button')
    button_save_cookie = (By.CSS_SELECTOR, '[data-testid="save-btn"]')
    button_search_icon = (By.CSS_SELECTOR, '[data-testid="little-search-icon"]')
    field_local = (By.CSS_SELECTOR, '[data-testid="structured-search-input-field-query"]')
    button_checkin = (By.CSS_SELECTOR, '[data-testid="structured-search-input-field-split-dates-0"]')
    button_initial_date = (By.CSS_SELECTOR, '[data-testid="calendar-day-04/09/2023"]')
    button_final_date = (By.CSS_SELECTOR, '[data-testid="calendar-day-10/09/2023"]')
    button_guests = (By.CSS_SELECTOR, '[data-testid="structured-search-input-field-guests-button"]')
    button_increase_adults = (By.CSS_SELECTOR, '[data-testid="stepper-adults-increase-button"]')
    button_search = (By.CSS_SELECTOR, '[data-testid="structured-search-input-search-button"]')
    card_content = (By.CSS_SELECTOR, '[data-testid="card-container"]')
    label_info = (By.CSS_SELECTOR, '[elementtiming="LCP-target"] span:last-child span')
    button_switch = (By.CSS_SELECTOR, '[role="switch"]')
    button_filter = (By.CSS_SELECTOR, '[data-testid="category-bar-filter-button"]')
    label_filter = (By.CSS_SELECTOR, '[aria-label="Filtros"] [elementtiming="LCP-target"] div')
    button_expand_map = (By.CSS_SELECTOR, '[aria-label="Expandir o mapa e recolher a lista de visualização"]')
    button_minimize_map = (By.CSS_SELECTOR, '[aria-label="Fechar mapa em tela cheia"]')
    label_show_list = (By.CSS_SELECTOR, '[aria-label="Fechar mapa em tela cheia"] div:last-child span')

    field_price_filter_min = (By.ID, 'price_filter_min')
    field_price_filter_max = (By.ID, 'price_filter_max')
    button_save_filters = (By.CSS_SELECTOR, '[role="dialog"] footer a')
    label_count_filters = (By.CSS_SELECTOR, 'button[data-testid="category-bar-filter-button"] ~ div div')
    button_2_rooms = (By.CSS_SELECTOR, '#menuItemButton-2 span')