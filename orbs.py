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

				# Once we reach the orbital section, start adding the orbitals to dicts (one for O and one for V)
				if "Orbital energies and kinetic energies (alpha):" in line:

					# Skip line after finding above string, as the line after this is the beginning of the orbital energies
					next(f)

					# Begin inner loop over the lines containing the orbital energies
					for inner_line in f:

						# Conditional block to check if we are at the end of the orbital energies
						# or at an occupied orbital, or at a virtual orbital
						if "Total kinetic energy from orbitals" in inner_line:
							break
						elif inner_line.split()[1] == "O":
							occup[int(inner_line.split()[0])] = float(inner_line.split()[2])
						elif inner_line.split()[1] == "V":
							virt[int(inner_line.split()[0])] = float(inner_line.split()[2])

	except FileNotFoundError:
		print("Sorry, the file was not found.")
	else:
		break

# Locate HOMO and LUMO energies from dictionaries

# Calculate HOMO-LUMO gap, convert to eV and print this information out