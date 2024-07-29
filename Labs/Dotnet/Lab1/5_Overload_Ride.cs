using System;
namespace lab
{
    internal class Overloading_Riding
    {
        class Shape
        {
            public string Name { get; }
            public Shape(string name)
            {
                Name = name;
            }
            public virtual void Display()
            {
                Console.WriteLine($"This is a {Name}");
            }
        }
        class Rectangle : Shape
        {
            public double Width { get; }
            public double Height { get; }
            public Rectangle(string name, double width, double height) : base(name)
            {
                Width = width;
                Height = height;
            }
            public override void Display()
            {
                base.Display();
                Console.WriteLine($"It has width: {Width} and height: {Height}");
            }
        }

        class Circle : Shape
        {
            public double Radius { get; }
            public Circle(string name, double radius) : base(name)
            {
                Radius = radius;
            }
            public void Display(double area)
            {
                Console.WriteLine($"This is a {Name} with radius {Radius}");
                Console.WriteLine($"Area: {area}");
            }
        }
        class Program
        {
            static void Main(string[] args)
            {
                Rectangle rectangle = new Rectangle("Rectangle", 5, 10); rectangle.Display();
                Circle circle = new Circle("Circle", 7);
                double circleArea = CalculateCircleArea(circle.Radius);
                circle.Display(circleArea);
            }
            static double CalculateCircleArea(double radius)
            {
                return Math.PI * Math.Pow(radius, 2);
            }
        }
    }
}

