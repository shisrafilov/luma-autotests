def test_buy_a_jacket(home, men_section, jackets, product, checkout):
    home.open_home_page()
    home.click_men_section()

    men_section.click_jackets_category()
    jackets.click_the_first_jacket()

    product.choose_size()
    product.choose_color()
    product.add_to_cart()
    product.wait_for_success_message()
    product.proceed_to_checkout()

    checkout.fill_in_shipping_data()
    checkout.click_next()
    checkout.place_order()
    checkout.expect_to_see_success_message()
