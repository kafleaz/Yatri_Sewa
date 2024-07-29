using System;
using System.Linq;
namespace lab
{
    internal class Linq
    {
        class Person
        {
            public string Name { get; set; }
            public int Age { get; set; }
        }
        class Program
        {
            static void Main(string[] args)
            {
                List<Person> people = new List<Person>
            {
                new Person { Name = "AZ", Age = 25 },                 
                new Person { Name = "Rajish", Age = 30 },
                new Person { Name = "Dev", Age = 22 }
            };
                var result = from person in people where IsAdult(person.Age) select person;

                Console.WriteLine("Adults:");
                foreach (var person in result)
                {
                    Console.WriteLine($"Name: {person.Name}, Age: {person.Age}");
                }
            }
            static bool IsAdult(int age)
            {
                return age >= 18;
            }
        }
    }
}
