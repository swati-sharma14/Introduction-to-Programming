📖 Scale Notes Generator 🎵

Welcome to the Scale Notes Generator! This code allows you to generate major and minor scales based on the root note you provide. 🎶


📝 Description

This code provides the following functionalities:

🎵 nodeCreate(): This function initializes the files to store the generated major and minor scales.

🎵 writeMajor(root): This function generates the major scale based on the given root note and writes it to the "scaleMajor.txt" file.

🎵 writeMinor(root): This function generates the minor scale based on the given root note and writes it to the "scaleMinor.txt" file.

🎵 majorNotes(root): This function reads the "scaleMajor.txt" file and displays the major scale for the given root note.

🎵 minorNotes(root): This function reads the "scaleMinor.txt" file and displays the minor scale for the given root note.


🛠️ Usage

1. Run the code.
2. The nodeCreate() function will create the necessary files to store the generated scales.
3. The writeMajor(root) and writeMinor(root) functions will generate the major and minor scales for each note in the Cnotes list, respectively, and write them to the corresponding files.
4. After the scales have been generated, the files (scaleMajor.txt and scaleMinor.txt) will be closed.
5. Enter the root note when prompted by the code.
6. Enter the type of scale (Major/Minor) when prompted by the code.
7. The code will display the generated scale in the key you specified.
