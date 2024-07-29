using System;
namespace lab
{
    internal class Use_Delegeate_Events
    {
        public delegate void EventHandler(string message); class Publisher
        {
            public event EventHandler Notify;
            public void DoSomething()
            {
                Console.WriteLine("Loading. . . . . ");
                Notify?.Invoke("Loaded Successfully.");
            }
        }
        class Subscriber
        {
            public void Subscribe(Publisher publisher)
            {
                publisher.Notify += HandleEvent;
            }
            public void Unsubscribe(Publisher publisher)
            {
                publisher.Notify -= HandleEvent;
            }
            private void HandleEvent(string message)
            {
                Console.WriteLine($"Event handled: {message}");
            }
        }
        class Program
        {
            static void Main(string[] args)
            {
                Publisher publisher = new Publisher();
                Subscriber subscriber = new Subscriber();

                subscriber.Subscribe(publisher); 
                publisher.DoSomething(); 
                subscriber.Unsubscribe(publisher); 
                publisher.DoSomething();
            }
        }
    }
}
