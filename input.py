prompts = [
    'Grind size: ',
    'Dose in: ',
    'Target ratio: ',
    'Output: ',
    'Preinfusion time: ',
    'Shot time: '
]

responses = []

for index, prompt in enumerate(prompts):
    response = input(str(index + 1) + '. ' + prompt)
    responses.append(response)

modification = input('Enter a number to modify or enter to continue: ')

while(modification != "" and int(modification) in range(1, len(prompts) + 1)):
    responses[int(modification) - 1] = input(modification +
                                             '. ' + prompts[int(modification) - 1])
    modification = input('Enter a number to modify or enter to continue: ')

grind_size = int(responses[0])
dose = float(responses[1])
target_ratio = float(responses[2])
target_output = target_ratio * dose
actual_output = float(responses[3])
actual_ratio = actual_output / dose
infusion_time = float(responses[4])
shot_time = float(responses[5])
total_time = infusion_time + shot_time
ratio_diff = (actual_ratio - target_ratio) / target_ratio
avg_flow = actual_output / shot_time

data = [grind_size, dose, target_ratio, target_output, actual_output,
        actual_ratio, infusion_time, shot_time, total_time, ratio_diff, avg_flow]

data_file = open('espresso.csv', 'a')
data_file.write(','.join(str(x) for x in data) + '\n')
data_file.close()

print("Shot data saved to espresso.csv")
