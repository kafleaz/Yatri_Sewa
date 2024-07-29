using System;
namespace lab
{
    internal class Basic_class_obj
    {
        class Person
        {
            public string? Name { get; set; }
            public int Age { get; set; }
            public void DisplayInfo()
            {
                Console.WriteLine($"Name: {Name}, Age: {Age}");
            }
        }

        class Program
        {
            static void Main(string[] args)
            {
                Person person1 = new Person(); 
                    person1.Name = "AZ"; 
                    person1.Age = 23;
                Person person2 = new Person(); 
                    person2.Name = "Rajish"; 
                    person2.Age = 24;
                Console.WriteLine("Person 1:");
                    person1.DisplayInfo(); 
                Console.WriteLine("\nPerson 2:"); 
                    person2.DisplayInfo();
            }
        }
    }
}

