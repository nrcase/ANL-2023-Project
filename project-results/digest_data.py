import os
import pandas as pd

control_folder = "./control/"
wolfpack_folder = "./wolfpack/"
lonewolf_folder = "./lonewolf/"
summary_output = "./summary.xlsx"

def combine_results(label, data_directory):
    # For all csvs in folder, read them into a separate df
    data = None
    for csv_file in os.scandir(data_directory):
        if csv_file.is_file():
            test = pd.read_csv(csv_file)
            test = test.rename(columns={"Unnamed: 0":"agent"})
            if data is None:
                data = test
            else:
                data = pd.concat((data, test), ignore_index=True)

    # Combine all dfs into a single df given averages of each agent
    data_combined = data.groupby(data['agent']).mean().sort_values('avg_utility', ascending=False)
    average_utility, std_avg_utility = data_combined.loc[:, 'avg_utility'].mean(), data_combined.loc[:, 'avg_utility'].std()
    average_social_welfare, std_social_welfare = data_combined.loc[:, 'avg_social_welfare'].mean(), data_combined.loc[:, 'avg_social_welfare'].std()
    print(label)
    print("Average Utility of All Agents:", round(average_utility, 3), "Standard Dev:", round(std_avg_utility, 3))
    print("Average Social Welfare of All Agents:", round(average_social_welfare, 3), "Standard Dev:", round(std_social_welfare, 3))
    return data_combined

# Digest the data
control_data = combine_results("Control", control_folder)
wolfpack_data = combine_results("WolfpackAgent", wolfpack_folder)
lonewolf_data = combine_results("LoneWolfAgent", lonewolf_folder)

# 3rd best in social welfare!
print(wolfpack_data.sort_values('avg_social_welfare', ascending=False))

# Below 50th percentile for avg_utility :(
print(lonewolf_data)

# Output summmary data for all tournament types
summary_data = pd.concat([control_data.mean(), control_data.std(), lonewolf_data.mean(), lonewolf_data.std(), wolfpack_data.mean(), wolfpack_data.std()], axis=1)
summary_data.columns = ['Control Mean', 'Control std', 'LoneWolfAgent Mean', 'LoneWolfAgent std', 'WolfpackAgent Mean', 'WolfpackAgent std']
summary_data.to_excel(summary_output)