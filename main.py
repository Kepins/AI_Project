from simulation import Simulation
import csv


def save_frames(frames):
    id_cur: int
    with open('simulations_run/independent/current_id.txt', 'r+') as f_txt:
        id_cur = int(f_txt.read())
        f_txt.truncate(0)
        f_txt.seek(0)
        f_txt.write(str(id_cur+1))

    with open('simulations_run/independent/data{id}.csv'.format(id=str(id_cur)), 'w', newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(['Height', 'Velocity', 'Power'])
        write.writerows(frames)

    with open('simulations_run/all_data.csv', 'a', newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerows(frames)


if __name__ == '__main__':
    Simulation.init()
    if Simulation.controller.status:
        result, frames = Simulation.run()
        if Simulation.rate():
            save_frames(frames)
    print("Game closed")
