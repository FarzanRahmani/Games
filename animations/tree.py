import turtle
#recrusive function
Min_branch = 9
def build_tree(t,branch_len,shorten_len,angle):
    if branch_len > Min_branch:
        t.fd(branch_len)
        new_branch_len = branch_len - shorten_len
        t.left(angle)
        build_tree(t,new_branch_len,shorten_len,angle)
        t.right(2*angle)
        build_tree(t,new_branch_len,shorten_len,angle)
        t.left(angle)
        t.backward(branch_len) #**backward = branch_len not new_branch_len**

tree = turtle.Turtle()
tree.hideturtle()
tree.seth(90)
tree.pencolor("green")
tree.speed(10)
build_tree(tree,50,5,40)
turtle.mainloop()
