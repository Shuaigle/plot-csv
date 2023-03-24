import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def convert_time(time_str):
    return datetime.strptime(time_str.replace('下午', 'PM').replace('上午', 'AM'), '%Y/%m/%d %p %I:%M:%S')


def main(file_path):
    # load the csv file
    df = pd.read_csv(file_path, parse_dates=['StartTime'])

    # apply the time conversion function
    df['StartTime'] = df['StartTime'].apply(convert_time)

    # create the plot
    fig, ax = plt.subplots()
    ax.plot(df['StartTime'], df['Voltage'], 'o-', label='Data')

    # customize the x-axis labels
    ticks = pd.date_range(df['StartTime'].min(), df['StartTime'].max(), freq='D')
    tick_labels = [tick.strftime('%Y/%m/%d %p %I:%M') for tick in ticks]
    plt.xticks(ticks, tick_labels)

    # set the plot labels and title
    ax.set_title('Power consumption')
    ax.set_xlabel('Date Time')
    ax.set_ylabel('Power(V)')
    ax.legend()

    # set the plot size
    fig.set_size_inches(12, 6)

    # save the output file
    output_path = file_path.replace('.csv', '.jpg')
    plt.savefig(output_path)

    # show the plot
    plt.show()

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    main(file_path)

