using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SpikeNetwork
{
    /// <summary>
    /// Спайковый нейрон
    /// </summary>
    public class SpikeNeuron
    {
        /// <summary>
        /// Разность потенциалов
        /// </summary>
        public double U = 0;

        /// <summary>
        /// Пороговое значение входного сигнала
        /// </summary>
        public double I_0 = 1;

        /// <summary>
        /// Сопротивление нейрона
        /// </summary>
        public double R = 1;

        /// <summary>
        /// Коэффициент преобразования входного сигнала в разность потенциалов
        /// </summary>
        public double k = 5;

        /// <summary>
        /// Коэффициент преобразования выходного сигнала в изменение разности потенциалов
        /// </summary>
        public double q = 0.4;

        /// <summary>
        /// Входные весовые коэффиценты
        /// </summary>
        public List<double> weights;

        /// <summary>
        /// Максимальная емкость энергии
        /// </summary>
        public double E_max = 1;

        /// <summary>
        /// Накопленная энергия
        /// </summary>
        public double E = 0;

        /// <summary>
        /// Входные сигналы тока
        /// </summary>
        public List<double> inputs;

        /// <summary>
        /// Выходной сигнал
        /// </summary>
        public double output = 0;

        /// <summary>
        /// Конструктор по количеству входов
        /// </summary>
        /// <param name="count">Количество входов (синапсов)</param>
        public SpikeNeuron(int count)
        {
            weights = new List<double>();
            inputs = new List<double>();

            for (int i = 1; i <= count; i++)
            {
                weights.Add(1);
                inputs.Add(0);
            }
        }

        /// <summary>
        /// Шаг моделирования
        /// </summary>
        public void step(double dE)
        {
            double I_in = 0;
            for (int i = 0; i < weights.Count; i++)
            {
                I_in += weights[i] * inputs[i];
            }

            /*output = U / R;
            U = U + k * (I_in >= I_0 ? I_in : 0) - q * output;*/

            E = E + k * dE;

            if (E > E_max)
                E = E_max;

            // условие генерации спайка
            if (I_in >= I_0) {
                U = U + E;
                E = 0;
            }

            output = U / R;

            // снижение напряжения из-за выходного сигнала
            U = U - q * output;
        }
    }
}
