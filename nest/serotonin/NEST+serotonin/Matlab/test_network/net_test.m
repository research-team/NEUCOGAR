% Simple network of leaky quadratic IAF-neurons (u,v) based on [net.m, Izhikevich]
% 1000 = 800 excitatory + 200 inhibitory neurons\
% u = membrane potential of the neyron
% v = membrane recovery

clear all;
clc;

% Excitatory neurons    Inhibitory neurons
Ne=800;                 Ni=200;
re=rand(Ne,1);          ri=rand(Ni,1);
a=[0.02*ones(Ne,1);     0.02+0.08*ri];
b=[0.2*ones(Ne,1);      0.25-0.05*ri];
c=[-65+15*re.^2;        -65*ones(Ni,1)];
d=[8-6*re.^2;           2*ones(Ni,1)];
S=[0.5*rand(Ne+Ni,Ne),  -rand(Ne+Ni,Ni)]; % synaptic connections pattern

v=-65*ones(Ne+Ni,1);    % Initial values of v
u=b.*v;                 % Initial values of u
firings=[];             % spike timings

t_max = 500;           % simulation time in [ms]

I_t = zeros(t_max, 1); % I of t
v_t = zeros(t_max, 1); % v of t
t_t = 1:t_max; % time

for t = 1:t_max
    %I = [5*randn(Ne,1); 2*randn(Ni,1)]; % random thalamic input
    I = [5*ones(Ne,1); 2*ones(Ni,1)]; % constant thalamic input
    
    fired = find(v >= 30);    % indices of spikes
    firings = [firings; t + 0 * fired, fired];
    v(fired) = c(fired);
    u(fired) = u(fired) + d(fired);
    
    I = I + sum(S(:, fired), 2);
    v = v + 0.5*(0.04*v.^2+5*v+140-u+I); % step 0.5 ms
    v = v + 0.5*(0.04*v.^2+5*v+140-u+I); % for numerical
    u = u + a.*(b.*v-u);                 % stability
    
    % save
    I_t(t, 1) = sum(I) ./ (Ne + Ni);
    v_t(t, 1) = sum(v) ./ (Ne + Ni);
    
    %   I_t(t, 1) = I(1,1);
    %   v_t(t, 1) = v(1,1);
end;

test = [1; 2]; % 2 rows, 1 column
test2 = [1, 2]; % 1 row, 2 columns

subplot(3, 1, 1)
plot(firings(:,1), firings(:,2), '.b');
title('Simulation of a network of 800(exc)+200(inh) randomly coupled spiking neurons');
xlabel('t, ms');
ylabel('neuron number');
grid off

subplot(3, 1, 2)
plot(t_t, v_t, 'k');
title('Membrane potential of the neyrons');
xlabel('t, ms');
ylabel('v(t), mV');
grid on

subplot(3, 1, 3)
plot(t_t, I_t, 'r');
title('Thalamic current input');
xlabel('t, ms');
ylabel('I(t)');
grid on