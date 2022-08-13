"""
Login
"""
# login_link_xpath = '//a[text()=" ورود "]'
username_textbox_name = '//input[@name="username"]'
continue_button_xpath = ''
password_textbox_xpath = '//input[@name="password"]'
login_button_xpath = '//button[@class="btn btn-default"]'
assert_login = '(//a[text()!=""])[2]'
assert_not_login = '//div[@class="col-sm-4 col-sm-offset-1"]/h3[text()="اطلاعات وارد شده نامعتبر می باشد."]'
"""
Search Hotel
"""
hotel_button_xpath = '//div[@class="tabs_text__6YpmA"] [text()="هتل"]'
hotelCity_selectBox_xpath = '//button[@data-test="hotelCitySelectBox"]'
cityList_xpath = '//*[@class="hotel-city-select_popoverContainer__WqBLr"]' \
                 '//*[@class="hotel-city-select_hotelCitiesListWrapper__mKfz8"]'
month_list_xpath = '//*[@class="calendar-body_monthTogether__oI0zh false"]/div[2]/div[2]/div[2]'
daysList_className = 'month_flexDayStyle__Sp81_'
confirmDatePiker_button_xpath = '//button[@class="button_primaryBtn__L9gAL footer_closeButton__AdqEJ"] [text()="تایید"]'
searchButton_button_xpath = '//button[@class="button_primaryBtn__L9gAL search-button"]'
hotelList_list_xpath = '//*[@class="col-12 col-lg-9"]/div/div[2]'
"""
Booking Hotel
"""
selectHotel_button_xpath = '(//*[text() = "جزئیات و انتخاب"])[1]'
selectRoom_button_xpath = '(//*[text() = "جزییات و رزرو"])[1]'
selectReserv_button_xpath = '//button[@data-test="hotelReserveButton"] [text()="رزرو"]'
showPassengerModal_button_xpath = '//button[@data-test="showPassengersModalButton"]'
passengerTable_table_xpath = '//*[@id="room-0"]/div[2]/div[2]/div[4]'
selectPassenger_button_xpath = '(//*[text()="انتخاب"])[1]'
continueHotel_button_xpath = '//button[@data-test="continueHotelProcess"] [text()="ادامه فرآیند خرید"]'

"""
passengers
"""
name_input_id = 'firstNameAdt0'
lastName_input_id = 'lastNameAdt0'
email_input_id = 'emailAdt0'
mobile_input_id = 'mobileNumberAdt0'

"""
confirm and payment
"""
rulseConfirm_checkbox_xpath = '//*[@id="__next"]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[5]/label/span/div'


"""
payment
"""
paymentSuccess_button_id = 'btn-success'
paymentFailed_button_id = 'btn-failed'
