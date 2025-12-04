import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 200)

def read_json():
    df = pd.read_json('orders_simple.json')
    return df


def cleaning_and_conversion(df):
    df["total_amount"]=df["total_amount"].str.replace('$','').astype("float64")
    df["shipping_days"]=df["shipping_days"].astype('int64')
    df["customer_age"]=df["customer_age"].astype('int64')
    df["rating"]=df["rating"].astype('float64')
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df

def replacing_an_existing_column(df):
    df['items_html'] = df['items_html'].str.replace("<b>"," ").str.replace("</b>"," ").str.replace("<br>"," ")
    return df

def no_coupon(df):
    df['coupon_used'] = df['coupon_used'].replace ( "" ,"no coupon")
    return df

def create_order_month(df):
    df = df.assign(
        order_month=df['order_date'].dt.month
        )
    return df

def create_high_value_order(df):
    temp=df["total_amount"].mean()
    df["high_value_order"] = temp > df["total_amount"]
    df=df.sort_values(by="total_amount",ascending=False)
    return df

def mean_rating(df):
    temp=df.groupby('country')["rating"].mean()
    df["mean_rating"]= df["country"].map(temp)

    return df

def del_rows(df: pd.DataFrame):
    df = df[(df["total_amount"]>1000) & (df["rating"]>4.5)]
    return df

def delivery_status(df: pd.DataFrame):
    df['delivery_status'] = df['shipping_days'].apply(lambda x: "delayed" if x>7 else "on time" )
    return df
def load_csv(df):
    df.to_csv("clean_orders_[322998881].csv")
    return df



