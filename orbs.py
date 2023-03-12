# Creating dictionaries to hold occupied and virtual orbital energies
occup = {}
virt = {}

# Ask user for the name of the file
# Open up the file and start reading it, if the file exists
while True:
	try:
		file_name = input("Please enter the name of the file to analyse: ")
		with open(file_name + ".log") as f:
			for line in f:
				if "Orbital energies and kinetic energies (alpha):" in line:
					next(f)
					for inner_line in f:
						print(inner_line)
	except FileNotFoundError:
		print("Sorry, the file was not found.")
	else:
		break

# Once we reach the orbital section, start adding the orbitals to dicts (one for O and one for V)

# Locate HOMO and LUMO energies from dictionaries

# Calculate HOMO-LUMO gap, convert to eV and print this information out