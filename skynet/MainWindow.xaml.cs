using Avalonia;
using Avalonia.Controls;
using Avalonia.Diagnostics.ViewModels;
using Avalonia.Interactivity;
using Avalonia.Markup.Xaml;
using System;
using System.Reactive;

namespace skynet
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            this.DataContext = new MenuCommands();
            this.AttachDevTools();
        }

        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }
    }
}
