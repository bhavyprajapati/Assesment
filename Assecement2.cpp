#include <iostream.h>
#include <conio.h>
#include <stdio.h>
#include <string.h>

// Class to represent Lecture details
class Lecture {
private:
    char lecturerName[50];
    char subjectName[50];
    char courseName[50];
    static int lecturerCount; // Static member to count number of lecturers

public:
    // Default constructor
    Lecture() {
        strcpy(lecturerName, "");
        strcpy(subjectName, "");
        strcpy(courseName, "");
    }
    
    // Parameterized constructor to assign initial values
    Lecture(const char* lName, const char* sName, const char* cName) {
        strcpy(lecturerName, lName);
        strcpy(subjectName, sName);
        strcpy(courseName, cName);
        lecturerCount++;
    }
    
    // Function to add lecture details
    void addLectureDetails() {
        clrscr();
        cout << "\n\n========== ADD LECTURE DETAILS ==========\n";
        cout << "Enter Lecturer Name: ";
        gets(lecturerName);
        
        cout << "Enter Subject Name: ";
        gets(subjectName);
        
        cout << "Enter Course Name: ";
        gets(courseName);
        
        lecturerCount++;
        cout << "\nLecture details added successfully!\n";
        cout << "Press any key to continue...";
        getch();
    }
    
    // Function to display name and lecture details
    void displayLectureDetails() const {
        cout << "\n----------------------------------------";
        cout << "\nLecturer Name: " << lecturerName;
        cout << "\nSubject Name: " << subjectName;
        cout << "\nCourse Name: " << courseName;
        cout << "\n----------------------------------------";
    }
    
    // Static function to get lecturer count
    static int getLecturerCount() {
        return lecturerCount;
    }
    
    // Static function to reset lecturer count (if needed)
    static void resetLecturerCount() {
        lecturerCount = 0;
    }
};

// Initialize static member
int Lecture::lecturerCount = 0;

// Function to display main menu
void displayMenu() {
    clrscr();
    cout << "========================================";
    cout << "\n      LECTURE MANAGEMENT SYSTEM";
    cout << "\n========================================";
    cout << "\n1. Add Lecture Details";
    cout << "\n2. Display All Lecture Details";
    cout << "\n3. Display Lecturer Count";
    cout << "\n4. Exit";
    cout << "\n========================================";
    cout << "\nPlease enter your choice (1-4): ";
}

// Main function
void main() {
    clrscr();
    
    // Create array to handle details of 5 lecturers
    Lecture lecturers[5];
    int choice, count = 0;
    char ch;
    
    do {
        displayMenu();
        cin >> choice;
        
        switch(choice) {
            case 1: // Add Lecture Details
                if(count < 5) {
                    lecturers[count].addLectureDetails();
                    count++;
                } else {
                    cout << "\nMaximum limit of 5 lecturers reached!";
                    cout << "\nPress any key to continue...";
                    getch();
                }
                break;
                
            case 2: // Display All Lecture Details
                clrscr();
                cout << "\n\n========== ALL LECTURE DETAILS ==========\n";
                if(count == 0) {
                    cout << "No lecture details available. Please add details first.\n";
                } else {
                    for(int i = 0; i < count; i++) {
                        lecturers[i].displayLectureDetails();
                    }
                    cout << "\n\nTotal Lecturers: " << Lecture::getLecturerCount();
                }
                cout << "\n\nPress any key to continue...";
                getch();
                break;
                
            case 3: // Display Lecturer Count
                clrscr();
                cout << "\n\n========== LECTURER COUNT ==========\n";
                cout << "Total number of lecturers: " << Lecture::getLecturerCount();
                cout << "\n\nPress any key to continue...";
                getch();
                break;
                
            case 4: // Exit
                cout << "\nThank you for using Lecture Management System!\n";
                break;
                
            default:
                cout << "\nInvalid choice! Please try again.";
                cout << "\nPress any key to continue...";
                getch();
        }
    } while(choice != 4);
    
    cout << "\nPress any key to exit...";
    getch();
}