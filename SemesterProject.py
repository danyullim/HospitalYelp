import turtle
from tkinter import *

# Use Yelp API


MainWindow = Tk()

def mdanderson():
    MainWindow.destroy()

    arrow = turtle.Turtle()

    # Line Color
    arrow.fillcolor("red")
    arrow.speed(0)
    arrow.width(15)

    # Fillm
    arrow.up()
    arrow.setposition(-320, 300)
    arrow.color("#dfdfdf")
    arrow.begin_fill()
    arrow.down()

    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.end_fill()

    # Streets --------------------------------------------------------------------------------------------------------------
    arrow.speed(0)
    arrow.color("white")
    arrow.up()
    arrow.right(125)
    arrow.setposition(-320, 700)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 600)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 500)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 400)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 300)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 200)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 0)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -200)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -300)
    arrow.down()
    arrow.forward(800)

    # Horizontal
    arrow.up()
    arrow.setposition(-320, 200)
    arrow.down()
    arrow.left(90)
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 50)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -250)
    arrow.down()
    arrow.forward(800)
    # 000000000
    arrow.up()
    arrow.setposition(-320, -400)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -550)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -700)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -850)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -900)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -1050)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -1200)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(0, 0)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Whataburger", font="Arial 20")


    arrow.up()
    arrow.setposition(300, -200)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Houston's", font="Arial 20")

    arrow.up()
    arrow.setposition(-300, 100)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Post Oak Grill", font="Arial 20")

    arrow.up()
    arrow.setposition(180, 200)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Le Peep", font="Arial 20")

    arrow.up()
    arrow.setposition(-125, 250)
    arrow.down()
    arrow.color("black")
    arrow.write("Map of Houston", font="Arial 40 bold")
    arrow.up()
    arrow.setposition(-125, 400)

    def whataburger():
        whata = Tk()

        Label(whata, text="Whataburger", bg="orange", font="Arial 14 bold").pack()
        Label(whata, text="Phone Number: 1.800.628.7437\nHours: 24 hours\nBest Known Meal: Burger", bg="orange").pack()

        whata.title("Whataburger")
        whata.configure(background="orange")
        whata.geometry("300x100")
        whata.mainloop()

    def houston():
        hous = Tk()

        Label(hous, text="Houston's", bg="grey", font="Arial 14 bold").pack()
        Label(hous, text="Phone Number: 713.975.1947\nHours: 3p.m. - 11p.m.\nBest Known Meal: Roast Beef Snadwich", bg="grey").pack()

        hous.title("Houston's")
        hous.configure(background="grey")
        hous.geometry("300x100")
        hous.mainloop()

    def postoak():
        post = Tk()

        Label(post, text="Post Oak Grill", bg="black", font="Arial 14 bold", fg="white").pack()
        Label(post, text="Phone Number: 713.993.9966\nHours: 12p.m. - 10:30p.m.\nBest Known Meal: Grilled Steak", bg="black", fg="white").pack()

        post.title("Post Oak Grill")
        post.configure(background="black")
        post.geometry("300x100")
        post.mainloop()

    def lepeep():
        peep = Tk()

        Label(peep, text="Le Peep", bg="green", font="Arial 14 bold").pack()
        Label(peep, text="Phone Number: 713.780.7337\nHours: 6a.m. - 4p.m.\nBest Known Meal: Breakfast Meals", bg="green").pack()

        peep.title("Le Peep")
        peep.configure(background="green")
        peep.geometry("300x100")
        peep.mainloop()

    mdander = Tk()
    Label(mdander, text="Click on any of the following:\n").pack()
    Button(mdander, text="Whataburger", command=whataburger).pack()
    Button(mdander, text="Houston's", command=houston).pack()
    Button(mdander, text="Post Oak Grill", command=postoak).pack()
    Button(mdander, text="Le Peep", command=lepeep).pack()

    mdander.title("mdanderson Cuisine")
    mdander.geometry("350x350")
    mdander.mainloop()

def houstonmethodist():
    MainWindow.destroy()

    arrow = turtle.Turtle()

    # Line Color
    arrow.fillcolor("red")
    arrow.speed(0)
    arrow.width(15)

    # Fill
    arrow.up()
    arrow.setposition(-320, 300)
    arrow.color("#dfdfdf")
    arrow.begin_fill()
    arrow.down()

    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.end_fill()

    # Streets ------------------------------------------------------------------------------------------------------
    arrow.speed(0)
    arrow.color("white")
    arrow.up()
    arrow.right(125)
    arrow.setposition(-320, 700)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 600)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 500)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 400)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 300)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 200)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 0)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -200)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -300)
    arrow.down()
    arrow.forward(800)

    # Horizontal
    arrow.up()
    arrow.setposition(-320, 200)
    arrow.down()
    arrow.left(90)
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 50)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -250)
    arrow.down()
    arrow.forward(800)
    # 000000000
    arrow.up()
    arrow.setposition(-320, -400)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -550)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -700)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -850)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -900)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -1050)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -1200)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(0, 0)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Lupe Torilla", font="Arial 20")

    arrow.up()
    arrow.setposition(50, -200)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Ninfas", font="Arial 20")

    arrow.up()
    arrow.setposition(-300, 100)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("El Tiempo Cantina", font="Arial 20")

    arrow.up()
    arrow.setposition(180, -100)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Torchy's Tacos", font="Arial 20")

    arrow.up()
    arrow.setposition(-125, 250)
    arrow.down()
    arrow.color("black")
    arrow.write("Map of Houston", font="Arial 40 bold")
    arrow.up()
    arrow.setposition(-125, 400)

    def ninfas():
        nin = Tk()
        Label(nin, text="Ninfas", bg="blue", fg="white", font="Arial 14 bold").pack()
        Label(nin, text="Phone Number: 713.228.1175\nHours: 11a.m. - 10p.m.\nBest Known Meal: Enchiladas", bg="blue", fg="white").pack()
        nin.title("Ninfas")
        nin.configure(background="blue")
        nin.geometry("300x100")
        nin.mainloop()

    def lupe():
        l = Tk()
        Label(l, text="Lupe Tortilla", bg="yellow", font="Arial 14 bold").pack()
        Label(l, text="Phone Number: 713.975.1947\nHours: 11a.m. - 11p.m.\nBest Known Meal: Best Quesadillas",
              bg="yellow").pack()
        l.title("Lupe Tortilla")
        l.configure(background="yellow")
        l.geometry("300x100")
        l.mainloop()

    def tiempo():
        t = Tk()
        Label(t, text="El Tiempo Cantina", bg="green", font="Arial 14 bold", fg="black").pack()
        Label(t, text="Phone Number: 713.681.3645\nHours: 11a.m. - 10:0p.m.\nBest Known Meal: Excellent Fajitas",
              bg="green", fg="black").pack()
        t.title("El Tiempo Cantina")
        t.configure(background="green")
        t.geometry("300x100")
        t.mainloop()

    def torchy():
        taco = Tk()
        Label(taco, text="Torchy's Tacos", bg="red", font="Arial 14 bold", fg="white").pack()
        Label(taco, text="Phone Number: 713.595.8226\nHours: 7a.m. - 10p.m.\nBest Known Meal: Elaborate Tacos",
              bg="red", fg="white").pack()
        taco.title("Torchy's Tacos")
        taco.configure(background="red")
        taco.geometry("300x100")
        taco.mainloop()

    houstonmethodist = Tk()
    Label(houstonmethodist, text="Click on any of the following:\n").pack()
    Button(houstonmethodist, text="Ninfa's", command=ninfas).pack()
    Button(houstonmethodist, text="Lupe Tortilla", command=lupe).pack()
    Button(houstonmethodist, text="El Tiempo Cantina", command=tiempo).pack()
    Button(houstonmethodist, text="Torchy's Tacos", command=torchy).pack()

    houstonmethodist.title("houstonmethodist Cuisine")
    houstonmethodist.geometry("350x350")
    houstonmethodist.mainloop()

def houstoncancerinstitute():
    MainWindow.destroy()

    arrow = turtle.Turtle()

    # Line Color
    arrow.fillcolor("red")
    arrow.speed(0)
    arrow.width(15)

    # Fill
    arrow.up()
    arrow.setposition(-320, 300)
    arrow.color("#dfdfdf")
    arrow.begin_fill()
    arrow.down()

    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.right(90)
    arrow.forward(630)
    arrow.end_fill()

    # Streets --------------------------------------------------------------------------------------------------------------
    arrow.speed(0)
    arrow.color("white")
    arrow.up()
    arrow.right(125)
    arrow.setposition(-320, 700)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 600)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 500)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 400)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 300)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 200)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 0)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -200)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -300)
    arrow.down()
    arrow.forward(800)

    # Horizontal
    arrow.up()
    arrow.setposition(-320, 200)
    arrow.down()
    arrow.left(90)
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, 50)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -100)
    arrow.down()
    arrow.forward(800)

    arrow.up()
    arrow.setposition(-320, -250)
    arrow.down()
    arrow.forward(800)
    # 000000000
    arrow.up()
    arrow.setposition(-320, -400)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -550)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -700)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -850)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -900)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -1050)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-320, -1200)
    arrow.down()
    arrow.forward(1500)

    arrow.up()
    arrow.setposition(-75, 145)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Panda Express", font="Arial 20")

    arrow.up()
    arrow.setposition(-300, -200)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Chang's houstoncancerinstitute Restaurant", font="Arial 20")

    arrow.up()
    arrow.setposition(-250, 90)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Hunan Chef", font="Arial 20")

    arrow.up()
    arrow.setposition(50, -100)
    arrow.down()
    arrow.color("red")
    arrow.circle(3)
    arrow.color("black")
    arrow.write("Fu's Garden", font="Arial 20")

    arrow.up()
    arrow.setposition(-125, 250)
    arrow.down()
    arrow.color("black")
    arrow.write("Map of Houston", font="Arial 40 bold")
    arrow.up()
    arrow.setposition(-125, 400)

    def panda():
        express = Tk()

        Label(express, text="Panda Express", bg="red", font="Arial 14 bold", fg="white").pack()
        Label(express, text="Phone Number: 713.263.7252\nHours: 10a.m. - 10p.m.\nBest Known Meal: Variety of Chicken", bg="red", fg="white").pack()

        express.title("Panda Express")
        express.configure(background="red")
        express.geometry("300x100")
        express.mainloop()

    def chang():
        chan = Tk()

        Label(chan, text="Chang's houstoncancerinstitute Restaurant", bg="yellow", font="Arial 14 bold").pack()
        Label(chan, text="Phone Number: 713.334.1888\nHours: 11a.m. - 10p.m.\nBest Known Meal: Pork Dumplings",
              bg="yellow").pack()

        chan.title("Chang's houstoncancerinstitute Restaurant")
        chan.configure(background="yellow")
        chan.geometry("300x100")
        chan.mainloop()

    def hunan():
        hun = Tk()

        Label(hun, text="Hunan Chef", bg="purple", font="Arial 14 bold", fg="white").pack()
        Label(hun, text="Phone Number: 713.984.8488\nHours: 12p.m. - 10:30p.m.\nBest Known Meal: Beef",
              bg="purple", fg="white").pack()

        hun.title("Hunan Chef")
        hun.configure(background="purple")
        hun.geometry("300x100")
        hun.mainloop()

    def fu():
        fus = Tk()

        Label(fus, text="Fu's Garden", bg="gold", font="Arial 14 bold").pack()
        Label(fus, text="Phone Number: 713.783.4419\nHours: 11a.m. - 10p.m.\nBest Known Meal: Desserts",
              bg="gold").pack()

        fus.title("Fu's Garden")
        fus.configure(background="gold")
        fus.geometry("300x100")
        fus.mainloop()

    htxcancer = Tk()
    Label(htxcancer, text="Click on any of the following:\n").pack()
    Button(htxcancer, text="Panda Express", command=panda).pack()
    Button(htxcancer, text="Chang's houstoncancerinstitute Restaurant", command=chang).pack()
    Button(htxcancer, text="Hunan Chef", command=hunan).pack()
    Button(htxcancer, text="Fu's Garden", command=fu).pack()

    htxcancer.title("houstoncancerinstitute Cuisine")
    htxcancer.geometry("350x350")
    htxcancer.mainloop()

def review():
    MainWindow.destroy()

    RevWindow = Tk()

    def review_function():

        SmallWindow = Tk()
        first = fn_entry.get()
        second = sn_entry.get()
        email = e_entry.get()
        restaurant = rn_entry.get()
        comment = rv_entry.get()
        rating = ra_entry.get()

        if rating == "1":
            number = "*"
        if rating == "2":
            number = "**"
        if rating == "3":
            number = "***"
        if rating == "4":
            number = "****"
        if rating == "5":
            number = "*****"

        name = "Thank you, " + str(first) + " " + str(second) + ". Your review has been recorded!"
        Label(SmallWindow, text=name).pack()

        RevWindow.destroy()

        review = "First Name: " + str(first) + "\nLast Name: " + str(second) + "\nEmail: " + str(
            email) + "\nRestaurant: " + str(restaurant) + "\nComments: " + str(comment) + "\nRating: " + str(number)
        Label(SmallWindow, text=review, font="bold").pack()
        SmallWindow.title("Review")
        SmallWindow.geometry("400x400")
        SmallWindow.mainloop()

    first_name = Label(RevWindow, text="First Name: ")
    first_name.grid(row=0, column=0)
    fn_entry = Entry(RevWindow)
    fn_entry.grid(row=0, column=1)

    second_name = Label(RevWindow, text="Last Name: ")
    second_name.grid(row=2, column=0)
    sn_entry = Entry(RevWindow)
    sn_entry.grid(row=2, column=1)

    email = Label(RevWindow, text="Email: ")
    email.grid(row=3, column=0)
    e_entry = Entry(RevWindow)
    e_entry.grid(row=3, column=1)

    res_name = Label(RevWindow, text="Restaurant Name: ")
    res_name.grid(row=4, column=0)
    rn_entry = Entry(RevWindow)
    rn_entry.grid(row=4, column=1)

    review = Label(RevWindow, text="Comments: ")
    review.grid(row=5, column=0)
    rv_entry = Entry(RevWindow)
    rv_entry.grid(row=5, column=1)

    my_button = Button(RevWindow, text="Submit", command=review_function)
    my_button.grid(row=13, column=1)

    # Ratings
    rating = Label(RevWindow, text="Rating(Out of 5): ")
    rating.grid(row=6, column=0)
    ra_entry = Entry(RevWindow)
    ra_entry.grid(row=6, column=1)

    notice = Label(RevWindow, text="*ALL FIELDS ARE REQUIRED")
    notice.grid(row=7, column=0)

    RevWindow.title("Review")
    RevWindow.geometry("410x280")
    RevWindow.mainloop()

Label(MainWindow, text="\nBest Cancer Research and Hospitals in Houston\n", font="Arial 32", bg="#ce2200", fg="white").pack()
photo = PhotoImage(file="yelpicon.gif")
label = Label(image=photo)
label.image = photo
label.pack()
Label(MainWindow, text="\n\nChoose a cuisine:\n", bg="#ce2200", fg="white").pack()
Button(MainWindow, text="M.D. Anderson", command=mdanderson).pack()
Button(MainWindow, text="Houston Cancer Institute", command=houstoncancerinstitute).pack()
Button(MainWindow, text="Houston Methodist", command=houstonmethodist).pack()
Button(MainWindow, text="Submit a Cancer Hospital Review", command=review).pack()

MainWindow.title("Yelp In Python")
MainWindow.geometry("1000x600+250+0")
MainWindow.configure(background="#ce2200")
MainWindow.mainloop()
