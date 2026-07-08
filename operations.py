import numpy as np
from tkinter import *

class operations:
    root = None
    parent = None
    header = None
    matrix_font = None
    text_font = None

    @classmethod
    def setRoot(cls, root, parent, header, matrix_font, text_font, frame_pos):
        cls.root = root
        cls.parent = parent
        cls.header = header
        cls.matrix_font = matrix_font
        cls.text_font = text_font

    @classmethod
    def clearUI(cls):
        for widget in cls.parent.winfo_children():
            if widget != cls.header:
                widget.destroy()

    @classmethod
    def showAdditionComponent(cls):
        cls.clearUI()

        frame = Frame(cls.parent, bg="green")
        frame.grid(row=0, column=1, padx=20)

        Label(
        frame,
        text="Matrix Addition",
        font=("Arial", 16, "bold"),
        bg="green",
        fg="white"
    ).pack(pady=10)

        Label(
        frame,
        text="Enter Matrix Size (Rows x Columns)",
        bg="green",
        fg="white"
    ).pack()

        size_frame = Frame(frame, bg="green")
        size_frame.pack(pady=5)

        rows = Entry(size_frame, width=5)
        rows.grid(row=0, column=0, padx=5)

        cols = Entry(size_frame, width=5)
        cols.grid(row=0, column=1, padx=5)

        Button(
            frame,
            text="Create Matrix",
            command=lambda: cls.createMatrixInputs(
                int(rows.get()),
                int(cols.get()),
                frame
        )
    ).pack(pady=10)

    @classmethod
    def createMatrixInputs(cls, r, c, frame):
      cls.matrixA = []
      cls.matrixB = []

      Label(
        frame,
        text="Matrix A",
        bg="green",
        fg="white"
    ).pack()

      for i in range(r):
            row = []
            row_frame = Frame(frame, bg="green")
            row_frame.pack()

            for j in range(c):
               entry = Entry(row_frame, width=5) 
               entry.pack(side=LEFT, padx=2)
               row.append(entry)
            cls.matrixA.append(row)

      Label(
            frame,
            text="Matrix B",
            bg="green",
            fg="white"
        ).pack(pady=10)

      for i in range(r):
            row = []
            row_frame = Frame(frame, bg="green")
            row_frame.pack()

            for j in range(c):
               entry = Entry(row_frame, width=5)
               entry.pack(side=LEFT, padx=2)
               row.append(entry)
            cls.matrixB.append(row)
      Button(
        frame,
        text="Add Matrix",
        command=lambda: 
        cls.addMatrix(r,c,frame)
    ).pack(pady=10)
            
    @classmethod
    def addMatrix(cls, r, c, frame):

        result = []

        for i in range(r):
             row = []

             for j in range(c):
                value = int(cls.matrixA[i][j].get()) + int(cls.matrixB[i][j].get())
                row.append(value)

             result.append(row)

        Label(
            frame,
            text="Result Matrix",
            bg="green",
            fg="white"
        ).pack()


        for row in result:
             Label(
                frame,
                text=str(row),
                bg="green",
                fg="white"
            ).pack()
             
    @classmethod
    def showSubtractionComponent(cls):
        cls.clearUI()

        frame = Frame(cls.parent, bg="green")
        frame.grid(row=0, column=1, padx=20)

        Label(
            frame,
            text="Matrix Subtraction",
            font=("Arial", 16, "bold"),
            bg="green",
            fg="white"
        ).pack(pady=10)

        Label(
            frame,
            text="Enter Matrix Size (Rows x Columns)",
            bg="green",
            fg="white"
        ).pack()

        size_frame = Frame(frame, bg="green")
        size_frame.pack(pady=5)

        rows = Entry(size_frame, width=5)
        rows.grid(row=0, column=0, padx=5)

        cols = Entry(size_frame, width=5)
        cols.grid(row=0, column=1, padx=5)

        Button(
            frame,
            text="Create Matrix",
            command=lambda: cls.createSubtractionInputs(
                int(rows.get()),
                int(cols.get()),
                frame
            )
        ).pack(pady=10)

    @classmethod
    def createSubtractionInputs(cls, r, c, frame):

        cls.matrixA = []
        cls.matrixB = []

        Label(
            frame,
            text="Matrix A",
            bg="green",
            fg="white"
        ).pack()


        for i in range(r):
            row = []
            row_frame = Frame(frame, bg="green")
            row_frame.pack()

            for j in range(c):
                entry = Entry(row_frame, width=5)
                entry.pack(side=LEFT, padx=2)
                row.append(entry)

            cls.matrixA.append(row)

        Label(
            frame,
            text="Matrix B",
            bg="green",
            fg="white"
        ).pack(pady=10)

        for i in range(r):
            row = []
            row_frame = Frame(frame, bg="green")
            row_frame.pack()

            for j in range(c):
                entry = Entry(row_frame, width=5)
                entry.pack(side=LEFT, padx=2)
                row.append(entry)

            cls.matrixB.append(row)

        Button(
            frame,
            text="Subtract Matrix",
            command=lambda: cls.subtractMatrix(r,c,frame)
        ).pack(pady=10)

    @classmethod
    def subtractMatrix(cls, r, c, frame):

        result = []

        for i in range(r):
            row = []

            for j in range(c):
                value = int(cls.matrixA[i][j].get()) - int(cls.matrixB[i][j].get())
                row.append(value)

            result.append(row)


        Label(
            frame,
            text="Result Matrix",
            bg="green",
            fg="white"
        ).pack()


        for row in result:
            Label(
                frame,
                text=str(row),
                bg="green",
                fg="white"
            ).pack()

    @classmethod
    def showMultiplicationComponent(cls):
        cls.clearUI()

        frame = Frame(cls.parent, bg="green")
        frame.grid(row=0, column=1, padx=20)

        Label(
            frame,
            text="Matrix Multiplication",
            font=("Arial", 16, "bold"),
            bg="green",
            fg="white"
        ).pack(pady=10)

        Label(
            frame,
            text="Enter Matrix Size (Rows x Columns)",
            bg="green",
            fg="white"
        ).pack()


        size_frame = Frame(frame, bg="green")
        size_frame.pack(pady=5)


        rows = Entry(size_frame, width=5)
        rows.grid(row=0, column=0, padx=5)


        cols = Entry(size_frame, width=5)
        cols.grid(row=0, column=1, padx=5)


        Button(
            frame,
            text="Create Matrix",
            command=lambda: cls.createMultiplicationInputs(
                int(rows.get()),
                int(cols.get()),
                frame
            )
        ).pack(pady=10)

    @classmethod
    def createMultiplicationInputs(cls, r, c, frame):

        cls.matrixA = []
        cls.matrixB = []


        Label(
            frame,
            text="Matrix A",
            bg="green",
            fg="white"
        ).pack()


        for i in range(r):
            row = []
            row_frame = Frame(frame, bg="green")
            row_frame.pack()

            for j in range(c):
                entry = Entry(row_frame, width=5)
                entry.pack(side=LEFT, padx=2)
                row.append(entry)

            cls.matrixA.append(row)

        Label(
            frame,
            text="Matrix B",
            bg="green",
            fg="white"
        ).pack(pady=10)

        for i in range(r):
            row = []
            row_frame = Frame(frame, bg="green")
            row_frame.pack()

            for j in range(c):
                entry = Entry(row_frame, width=5)
                entry.pack(side=LEFT, padx=2)
                row.append(entry)

            cls.matrixB.append(row)

        Button(
            frame,
            text="Multiply Matrix",
            command=lambda: cls.multiplyMatrix(r,c,frame)
        ).pack(pady=10)

    @classmethod
    def multiplyMatrix(cls, r, c, frame):

        result = []

        for i in range(r):
            row = []

            for j in range(c):
                value = 0

                for k in range(c):
                    value += int(cls.matrixA[i][k].get()) * int(cls.matrixB[k][j].get())

                row.append(value)

            result.append(row)

        Label(
            frame,
            text="Result Matrix",
            bg="green",
            fg="white"
        ).pack()

        for row in result:
            Label(
                frame,
                text=str(row),
                bg="green",
                fg="white"
            ).pack()

    @classmethod
    def showTransposeComponent(cls):
        cls.clearUI()

        frame = Frame(cls.parent, bg="green")
        frame.grid(row=0, column=1, padx=20)


        Label(
            frame,
            text="Matrix Transpose",
            font=("Arial", 16, "bold"),
            bg="green",
            fg="white"
        ).pack(pady=10)


        Label(
            frame,
            text="Enter Matrix Size (Rows x Columns)",
            bg="green",
            fg="white"
        ).pack()

        size_frame = Frame(frame, bg="green")
        size_frame.pack(pady=5)

        rows = Entry(size_frame, width=5)
        rows.grid(row=0, column=0, padx=5)

        cols = Entry(size_frame, width=5)
        cols.grid(row=0, column=1, padx=5)

        Button(
            frame,
            text="Create Matrix",
            command=lambda: cls.createTransposeInputs(
                int(rows.get()),
                int(cols.get()),
                frame
            )
        ).pack(pady=10)

    @classmethod
    def createTransposeInputs(cls, r, c, frame):

        cls.matrix = []

        Label(
            frame,
            text="Matrix",
            bg="green",
            fg="white"
        ).pack()


        for i in range(r):
            row = []

            row_frame = Frame(frame, bg="green")
            row_frame.pack()

            for j in range(c):
                entry = Entry(row_frame, width=5)
                entry.pack(side=LEFT, padx=2)
                row.append(entry)


            cls.matrix.append(row)

        Button(
            frame,
            text="Transpose Matrix",
            command=lambda: cls.transposeMatrix(r,c,frame)
        ).pack(pady=10)

    @classmethod
    def transposeMatrix(cls, r, c, frame):

        Label(
            frame,
            text="Result Matrix",
            bg="green",
            fg="white"
        ).pack()

        for j in range(c):

            row = []

            for i in range(r):
                row.append(cls.matrix[i][j].get())

            Label(
                frame,
                text=str(row),
                bg="green",
                fg="white"
            ).pack()

    @classmethod
    def showDeterminantComponent(cls):
        cls.clearUI()

        frame = Frame(cls.parent, bg="green")
        frame.grid(row=0, column=1, padx=20)

        Label(
            frame,
            text="Matrix Determinant",
            font=("Arial", 16, "bold"),
            bg="green",
            fg="white"
        ).pack(pady=10)

        Label(
            frame,
            text="Enter Matrix Size (Only Square Matrix)",
            bg="green",
            fg="white"
        ).pack()

        size = Entry(frame, width=5)
        size.pack(pady=5)

        Button(
            frame,
            text="Create Matrix",
            command=lambda: cls.createDeterminantInputs(
                int(size.get()),
                frame
            )
        ).pack(pady=10)

    @classmethod
    def createDeterminantInputs(cls, n, frame):

        cls.detMatrix = []

        Label(
            frame,
            text="Matrix",
            bg="green",
            fg="white"
        ).pack()

        for i in range(n):

            row = []

            row_frame = Frame(frame, bg="green")
            row_frame.pack()

            for j in range(n):

                entry = Entry(row_frame, width=5)
                entry.pack(side=LEFT, padx=2)
                row.append(entry)


            cls.detMatrix.append(row)

        Button(
            frame,
            text="Find Determinant",
            command=lambda: cls.calculateDeterminant(n, frame)
        ).pack(pady=10)

    @classmethod
    def calculateDeterminant(cls, n, frame):

        matrix = []

        for i in range(n):

            row = []

            for j in range(n):

                row.append(int(cls.detMatrix[i][j].get()))

            matrix.append(row)

        result = round(np.linalg.det(matrix))

        Label(
            frame,
            text="Determinant = " + str(result),
            bg="green",
            fg="white"
        ).pack(pady=10)

    @classmethod
    def showMessage(cls, text):
        cls.clearUI()
        frame = Frame(cls.parent, bg="green")
        frame.grid(row=0, column=1, padx=20)

        Label(
            frame,
            text=text,
            font=("Arial", 16, "bold"),
            bg="green",
            fg="white"
        ).pack(pady=20)