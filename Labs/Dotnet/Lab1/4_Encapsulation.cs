using System;
namespace lab
{
    internal class Encapsulation
    {
        class Student
        {
            private string[] subjects = new string[5]; 
            public string this[int index]
            {
                get { return subjects[index]; }
                set { subjects[index] = value; }
            }
            public int TotalSubjects
            {
                get { return subjects.Length; }
            }
        }

        class Program
        {
            static void Main(string[] args)
            {
                Student student = new Student(); 
                    student[0] = "Math"; 
                    student[1] = "Science"; 
                    student[2] = "History";     
                    student[3] = "English"; 
                    student[4] = "Computer Science"; 
                Console.WriteLine("Subjects:");

                for (int i = 0; i < student.TotalSubjects; i++)
                {
                    Console.WriteLine($"Subject {i + 1}: {student[i]}");
                }
            }
        }
    }
}
