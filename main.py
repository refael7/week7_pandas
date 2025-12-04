from utils import read_json, cleaning_and_conversion, replacing_an_existing_column, no_coupon, create_order_month, \
    create_high_value_order, mean_rating, load_csv, delivery_status, del_rows


def main():
    print("question 0")
    print("read_json")
    df=read_json()
    print("question 1")
    print("cleaning_and_conversion")
    df=cleaning_and_conversion(df)
    print("question 2")
    print("replacing_an_existing_column")
    df=replacing_an_existing_column(df)
    print("question 3")
    print("no_coupon")
    df=no_coupon(df)
    print("question 4")
    print("create_order_month")
    df=create_order_month(df)
    print("question 5")
    print("create_high_value_order")
    df=create_high_value_order(df)
    print("question 6")
    print("mean_rating")
    df=mean_rating(df)
    print("question 7")
    print("del_rows")

    df = del_rows(df)

    print("question 8")
    print("delivery_status")
    df=delivery_status(df)

    print("question 9")
    print("load_csv")
    load_csv(df)
    print(df)
















if __name__ == "__main__":
    main()