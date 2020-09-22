concertSeats=[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 211, 12],
  [13, 14, 15]
]

#def to check viewability
def checkView(concertSeats):
    for cols in range(len(concertSeats[0])):
        view=True
        for rows in range(len(concertSeats)-1):
            if concertSeats[rows][cols] < concertSeats[rows+1][cols]:
                print('The True values being compared are: ', concertSeats[rows][cols] , concertSeats[rows+1][cols])
                view=True
            else:
                print('The False values being compared are: ', concertSeats[rows][cols] , concertSeats[rows+1][cols])
                view=False 
                break
        if view==True: 
            print("All people is the column: ", cols+1 , 'can view')

#main 
checkView(concertSeats)