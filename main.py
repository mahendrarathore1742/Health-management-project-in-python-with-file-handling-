import datetime as d1;
def name_of_clients():
    print('select the name');
    print('-------------------------------------------------');
    print(' client1=> 1 \n client2=> 2 \n client3=> 3');
    print('-------------------------------------------------');
    name=(input('enter the value==>'));
    print('-------------------------------------------------');
    print('-------------------------------------------------');
    #this is first client information write
    if name=='1':
        print('select the option')
        print('-------------------------------------------------');
        print('-for yoga press 1- \n -for food press 2-');
        print('-------------------------------------------------');
        option=input('enter the value==>');
        print('-------------------------------------------------');

        #this is first client information write exercise
        if option=="1":
            with open(' enter the your path exercise for client.txt','w') as file:
                date=d1.datetime.now();
                information={'date':date, 'name':"client1",'exercise':[input('enter the exercise==>')]};
                information=str(information);
                file.write(information);
                file.close();
        #this is first client information write food

        elif option=="2":
            with open('enter the your path exercise for client_food.txt','w') as file:
                date=d1.datetime.now();
                information={'date':date, 'name':"client1",'food':[input('enter the food type==>')]};
                information=str(information);
                file.write(information);
                file.close();
        else:
            print('-option is not found-');

    #this is second client information write

    elif name=='2':

        print('select the option')
        print('-------------------------------------------------');
        print('-for yoga press 1- \n -for food press 2-');
        print('-------------------------------------------------');
        option=input('enter the value==>');
        print('-------------------------------------------------');

        #this is second client information write exercise

        if option=="1":
            with open('enter the your path exercise for client2.txt_exercise.txt','w') as file:
                date=d1.datetime.now();
                information={'date':date, 'name':"client2",'exercise':[input('enter the exercise==>')]};
                information=str(information);
                file.write(information);
                file.close();

        #this is second client information write food

        elif option=="2":
            with open('enter the your path exercise for client2_food.txt','w') as file:
                date=d1.datetime.now();
                information={'date':date, 'name':"client2",'food':[input('enter the food type==>')]};
                information=str(information);
                file.write(information);
                file.close();

       #this is theard client information write

    elif name=="3":
        print('select the option')
        print('-------------------------------------------------');
        print('-for yoga press 1- \n -for food press 2-');
        print('-------------------------------------------------');
        option=input('enter the value==>');
        print('-------------------------------------------------');
        #this is theard client information write exercise
        if option=="1":
            with open('Center the your path exercise for client3_exercise.txt','w') as file:
                date=d1.datetime.now();
                information={'date':date, 'name':"client3",'exercise':[input('enter the exercise==>')]};
                information=str(information);
                file.write(information);
                file.close();

        #this is theard client information write food
        elif option=="2":
            with open('enter the your path exercise for client3_food.txt','w') as file:
                date=d1.datetime.now();
                information={'date':date, 'name':"clien3",'food':[input('enter the food type==>')]};
                information=str(information);
                file.write(information);
                file.close();
        else:
            print('-option is not found-');
    else:
        print('-name is not found-')
#----------------------------------------------------------------------------------------------------------------------------------------
def read_info():
    print('------------------------------------------');
    print('select the name');
    print('-------------------------------------------------');
    print(' client1 => 1 \n client1=> 2 \n client1=> 3');
    print('-------------------------------------------------');
    name=(input('enter the value for read file==>'));

    print('-------------------------------------------------');
    print('-------------------------------------------------');
    #this is first client information read
    if name=='1':
        print('select the option')
        print('-------------------------------------------------');
        print('-for yoga file press 1- \n -for food file press 2-');
        print('-------------------------------------------------');
        option=input('enter the value==>');
        print('-------------------------------------------------');

        if option=="1":
            with open('enter the path client1_exercise.txt','r') as file:
                print(file.read());
            
        elif option=='2':
            with open('enter the path client1_food.txt','r') as file:
                print(file.read());
        else:
            print('-option is not found-');
    elif name=='2':
        print('select the option')
        print('-------------------------------------------------');
        print('-for yoga file press 1- \n -for food file press 2-');
        print('-------------------------------------------------');
        option=input('enter the value==>');
        print('-------------------------------------------------');

        if option=="1":
            with open('enter the path client2_exercise.txt','r') as file:
                print(file.read());
            
        elif option=='2':
            with open('Center the path client2_food.txt','r') as file:
                print(file.read());
        else:
            print('-option is not found-');

    elif name=='3':
        print('select the option')
        print('-for yoga file press 1- \n -for food file press 2-');
        option=input('enter the value==>');

        if option=="1":
            with open('enter the path client3_exercise.txt','r') as file:
                print(file.read(),'\n');
            
        elif option=='2':
            with open('enter the path client3_food.txt','r') as file:
                print(file.read());
        else:
            print('-option is not found-');
def main():
    print('--welcome to healt management system--\n\n --select the your ACTIVITY-- \n\n WRITE information to press 1>> \n\n READ information press 2>>\n\n');
    select=input('enter the your option-->>');

    if select=='1':
        name_of_clients();

    elif select=='2':
        read_info();

    else:
        print('<-option is not found->');
    print('-------------------------------------------------');
    print('continue your work so press Y/N');
    print('-------------------------------------------------');
    option=input('enter the option=>>');
    print('-------------------------------------------------');
    if option=="Y":
        main();
    elif option=='N':
        return 'have a good day';
    else:
        print('not option found');
main();