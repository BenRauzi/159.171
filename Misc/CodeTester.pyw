from tkinter import *
from tkinter import ttk
from tkinter.font import Font

class MainWindow:
	def __init__(self):
		self.root= Tk()
		self.root.title("191.171 Codetester")

		heading = ttk.Label(self.root, text="Enter the grid size:")
		heading.grid(row=0, column=0, columnspan=2 )

		label = ttk.Label(self.root, text="Enter the output from your program:")
		label.grid(row=1, column=0)

		self.user_entry = Text(self.root, height=8, width=50)
		self.user_entry.grid(row=2, column=0)

		label_expected = ttk.Label(self.root, text="Expected output from Coderunner:")
		label_expected.grid(row=1, column=1)

		self.expected_entry = Text(self.root, height=8, width=50)
		self.expected_entry.grid(row=2, column=1)

		enter_button = ttk.Button(self.root, width=135, text="Compare", command=self.compare)
		enter_button.grid(row=3, column=0, columnspan=2)

		self.output_frame = ttk.Frame(self.root, width=100)

		self.output = StringVar()
		output_label = ttk.Label(self.output_frame, textvariable=self.output)
		output_label.grid(row=0, column=0, columnspan=2)

		label = ttk.Label(self.output_frame, text="Expected:")
		label.grid(row=1, column=0)

		self.user_entry_output = Text(self.output_frame, height=8, width=50)
		self.user_entry_output.grid(row=2, column=1)

		label_expected = ttk.Label(self.output_frame, text="Got:")
		label_expected.grid(row=1, column=1)

		self.expected_entry_output = Text(self.output_frame, height=8, width=50)
		self.expected_entry_output.grid(row=2, column=0)

		self.bold_font = Font(family="Helvetica", size=14, weight="bold")

		self.user_entry_output.tag_configure("RED", background="red")
		self.expected_entry_output.tag_configure("RED", background="red")

		self.root.mainloop()

	def hide_label(self):
		self.output_frame.grid_forget()

	def show_label(self):
		self.output_frame.grid(row=4, column=0, columnspan=2)
		
	def compare(self):
		user_entry = self.user_entry.get("1.0",END)
		expected_entry = self.expected_entry.get("1.0",END)

		if user_entry == expected_entry:
			self.output.set("True - This is a valid input")
			self.show_label()
		else:
			num_longer = (max(len(expected_entry), len(user_entry)) - min(len(expected_entry), len(user_entry)))
			output_details = ""
			if len(user_entry) > len(expected_entry):
				output_details =  " - User output should be {} chars shorter".format(num_longer)
				expected_entry = expected_entry[:-1]
				expected_entry += "•" * num_longer + "\n"
			elif len(user_entry) < len(expected_entry):
				user_entry = user_entry[:-1]
				user_entry += "•" * num_longer + "\n"
				output_details =  " - User output should be {} chars longer".format(num_longer)

			self.output.set("False - This is an invalid input " + output_details)
			self.show_label()
		
		self.user_entry_output.delete("1.0", END)
		self.expected_entry_output.delete("1.0", END)

		for i in range(len(user_entry)):
			if expected_entry[i] == user_entry[i]:
				self.user_entry_output.insert(END,user_entry[i])
				self.expected_entry_output.insert(END,expected_entry[i])
			else:
				self.user_entry_output.insert(END,user_entry[i], "RED")
				self.expected_entry_output.insert(END,expected_entry[i], "RED")

MainWindow()