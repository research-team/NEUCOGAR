using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace SpikeNetwork
{
    public partial class MainForm : Form
    {
        /// <summary>
        /// Массив сигналов
        /// </summary>
        private List<double> signals;

        /// <summary>
        /// Массив сигналов нейрона
        /// </summary>
        private List<double> neuron_signals;
        
        /// <summary>
        /// Количество элементов в массиве сигналов (длина временной шкалы)
        /// </summary>
        private int count = 100;

        /// <summary>
        /// Текущий нейрон
        /// </summary>
        private SpikeNeuron neuron; 

        /// <summary>
        /// Признак того, что нажата кнопка мыши
        /// </summary>
        private bool mouse_spike_pressed = false;

        public MainForm()
        {
            InitializeComponent();
            signals = new List<double>();
            neuron_signals = new List<double>();
            for (int i = 1; i <= count; i++)
            {
                signals.Add(0);
                neuron_signals.Add(0);
            }
            neuron = new SpikeNeuron(3);
            neuron.weights[1] = 0.801; // коэффицент синаптической связи
            neuron.weights[2] = -1;
        }

        private void draw_graph()
        {
            chart.Series[1].Points.Clear();
            chart.Series[0].Points.Clear();
            for (int i = 1; i <= count; i++)
            {
                chart.Series[1].Points.AddXY(i, signals[i-1]);
                chart.Series[0].Points.AddXY(i, neuron_signals[i - 1]);
            }
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            if (mouse_spike_pressed) signals[count - 1] = 1; else signals[count - 1] = 0;
            neuron.inputs[0] = signals[count - 1];
            neuron.step(0.1);
            neuron.inputs[1] = neuron.output;
            neuron_signals[count - 1] = neuron.output;
            for (int i = 0; i < count-1; i++)
            {
                signals[i] = signals[i+1];
                neuron_signals[i] = neuron_signals[i + 1];
            }
            draw_graph();
        }

        private void btnSpike_MouseDown(object sender, MouseEventArgs e)
        {
            mouse_spike_pressed = true;
        }

        private void btnSpike_MouseUp(object sender, MouseEventArgs e)
        {
            mouse_spike_pressed = false;
        }

        private void btnReset_MouseDown(object sender, MouseEventArgs e)
        {
            neuron.inputs[2] = 1;
        }

        private void btnReset_MouseLeave(object sender, EventArgs e)
        {
            neuron.inputs[2] = 0;
        }
    }
}
