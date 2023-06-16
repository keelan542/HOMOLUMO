# Import statements
import sys
import matplotlib.pyplot as plt

# Creating lists to hold occupied and virtual orbital energies
occup = []
virt = []

# Ask user for the name of the file
# Open up the file and start reading it, if the file exists
try:
	file_name = input("Please enter the name of the file to analyse, without the .log extension: ")
	with open(file_name + ".log") as f:

		for line in f:

			# Once we reach the orbital section, start adding the orbitals to lists (one for O and one for V)
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
						occup.append(float(inner_line.split()[2]))
					elif inner_line.split()[1] == "V":
						virt.append(float(inner_line.split()[2]))

except FileNotFoundError:
	print("Sorry, the file was not found.")
	sys.exit()

# Locate HOMO and LUMO energies from lists
HOMO = occup[-1] * 27.211
LUMO = virt[0] * 27.211

# Calculate HOMO-LUMO gap, convert to eV and print this information out
gap = (LUMO - HOMO)
print("The HOMO energy is {:0.2f} eV".format(HOMO))
print("The LUMO energy is {:0.2f} eV".format(LUMO))
print("The HOMO-LUMO gap is {:0.2f} eV".format(gap))

# Placing HOMO and LUMO into list
homo_lumo = [HOMO, LUMO]

# Plotting code
plt.plot([1,1], homo_lumo, marker='_', markersize=35, linestyle='None')
plt.tick_params('x', labelbottom=False, bottom=False)
plt.title('Orbital Energy Plot')
plt.ylabel('Orbital Energy [eV]')
for i in range(2):
	plt.text(1, homo_lumo[i], '{:0.2f}'.format(homo_lumo[i]))
plt.show()