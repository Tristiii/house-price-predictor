from train import train_model
from predict import predict_price

print('I am a house price predictor.')
r2, mae, rmse = train_model()
print(f'Accuracy:\n',
      f'- R-squared (R^2): {round(r2, 2)}\n',
      f'- Mean absolute error (MAE): {round(mae, 2)}\n',
      f'- Root mean squared error (RMSE): {round(rmse, 2)}\n'
)

online = True
while online:
    i = input('Enter command: ')

    match i.split():
        case ['quit']:
            online = False
        case ['predict']:
            labels = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
            data = []

            for label in labels:
                filled = False
                while not filled:
                    try:
                        i = float(input(label + ': '))
                    except ValueError:
                        continue
                    else:
                        data.append(i)
                        filled = True

            print(predict_price(data))
        case ['predict', *values] if len(values) == 8:
            try:
                data = [float(v) for v in values]
            except ValueError:
                print('Please insert numbers as values.')
            else:
                print(predict_price(data))
        case _:
            print('I do not recognize that command.')