M=100;                 % number of synapses per neuron
D=1;                   % maximal conduction delay
% excitatory neurons   % inhibitory neurons      % total number
Ne=800;                Ni=200;                   N=Ne+Ni;
a=[0.02*ones(Ne,1);    0.1*ones(Ni,1)];
d=[   8*ones(Ne,1);    2*ones(Ni,1)];
sm=5;                 % maximal synaptic strength

post=ceil([N*rand(Ne,M);Ne*rand(Ni,M)]);
s=[ones(Ne,M);-ones(Ni,M)];         % synaptic weights
sd=zeros(N,M);                      % their derivatives
for i=1:N
    if i<=Ne
        for j=1:D
            delays{i,j}=M/D*(j-1)+(1:M/D);
        end;
    else
        delays{i,1}=1:M;
    end;
    pre{i}=find(post==i&s>0);             % pre excitatory neurons
    aux{i}=N*(D-1-ceil(ceil(pre{i}/N)/(M/D)))+1+mod(pre{i}-1,N);
end;
STDP = zeros(N,1001+D);
v = -65*ones(N,1);                      % initial values
u = 0.2.*v;                             % initial values
firings=[-D 0];                         % spike timings

%---------------
% new stuff related to DA-STDP
T=100;           % the duration of experiment
DA=0;           % level of dopamine above the baseline
ST=0;           % level of serotonine (5-HT)
ST_lim_fade_rate = 0.999;
ST_fade_rate = 0.999; 
DAnST_t = zeros(1000*T,2); % DA and ST of time
rew=[];
pun=[];

n1=1;           % presynaptic neuron
syn=1;          % the synapse number to the postsynaptic neuron
n2=post(n1,syn) % postsynaptic neuron
s(n1,syn)=0;    % start with 0 value

interval = 20;  % the coincidence interval for n1 and n2
interval2 = 40;
n1f=-100;       % the last spike of n1
n2f=[];         % the last spike of n2
SnSd_t=zeros(1000*T,2);
%--------------

for sec=1:T                             % simulation in seconds
    for t=1:1000                          % simulation of 1 sec
        I=13*(rand(N,1)-0.5);               % random thalamic input
        fired = find(v>=30);                % indices of fired neurons
        v(fired)=-65;
        u(fired)=u(fired)+d(fired);
        STDP(fired,t+D)=0.1;
        for k=1:length(fired)
            sd(pre{fired(k)})=sd(pre{fired(k)})+STDP(N*t+aux{fired(k)});
        end;
        firings=[firings;t*ones(length(fired),1),fired];
        k=size(firings,1);
        while firings(k,1)>t-D
            del=delays{firings(k,2),t-firings(k,1)+1};
            ind = post(firings(k,2),del);
            I(ind)=I(ind)+s(firings(k,2), del)';
            sd(firings(k,2),del)=sd(firings(k,2),del)-1.5*STDP(ind,t+D)';
            k=k-1;
        end;
        v=v+0.5*((0.04*v+5).*v+140-u+I);    % for numerical
        v=v+0.5*((0.04*v+5).*v+140-u+I);    % stability time
        u=u+a.*(0.2*v-u);                   % step is 0.5 ms
        STDP(:,t+D+1)=0.95*STDP(:,t+D);     % tau = 20 ms
        
        DA=DA*0.995;
        ST=ST*ST_fade_rate;
        if (mod(t,10)==0) % each 10 s
            s(1:Ne,:)=max(0, min(sm,s(1:Ne,:)+(0.002+DA)*sd(1:Ne,:)+(0.002+ST)*sd(1:Ne,:))); %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%!!!!!!!!!!!!!!!!!
            sd=0.99*sd;
        end;
        if any(fired==n1) % if presynaptic neuron has fired
            n1f=[n1f,sec*1000+t]; % the last spike of n1
        end
        if any(fired==n2) % if postsynsptic neyron has fired
            n2f=[n2f,sec*1000+t]; % the last spike of n2
            if (sec*1000+t-n1f(end)<interval) & (n2f(end)>n1f(end))
                rew=[rew,sec*1000+t+1000+ceil(2000*rand)];
            end;
            if (sec*1000+t-n1f(end)<interval2) & (n2f(end)>n1f(end))
                pun=[pun,sec*1000+t+1000+ceil(2000*rand)];
            end;
        end
	Pnov = 0.5 % check
	Ppun = 0.5 % check
        if any(rew==sec*1000+t)
            DA=DA+0.5; % why 0.5
            ST=ST+0.5;
	    NA=(DA+ST)*Pnov;
            %ST_fade_rate = ST_fade_rate + 0.01 %
        end;
        if any(pun==sec*1000+t)
            %ST_fade_rate = ST_fade_rate - 0.01 %
	    NA=ST*Ppun*Pnov;
            ST = ST-0.5;

        end;
        
        ST_fade_rate = min(ST_lim_fade_rate, ST_fade_rate);
        %ST = max(0, ST);
        
        SnSd_t(sec*1000+t,:) = [s(n1,syn), sd(n1,syn)]; % SnSd_t = [s, sd]
        DAnST_t(sec*1000+t,:) = [DA, max(0, ST)];
        % where s = synaptic weight, sd = eligibility trace
        
    end;
    % ---- plot -------
%     subplot(2,1,2)
%     plot(firings(:,1), firings(:,2), '.b');
%     axis([0 1000 0 N]);
%     title('Simulation of a network of 800(exc)+200(inh) randomly coupled spiking neurons');
%     xlabel('t, ms');
%     ylabel('neuron number');
%     grid off
    
    %subplot(2,1,1);
    plot(0.001*(1:(sec*1000+t)), SnSd_t(1:sec*1000+t,1), 'b', ...
        0.001*(1:(sec*1000+t)), SnSd_t(1:sec*1000+t,2), 'g--', ...
        0.001*(1:(sec*1000+t)), DAnST_t(1:sec*1000+t,1), 'm', ...
        0.001*(1:(sec*1000+t)), DAnST_t(1:sec*1000+t,2), 'c', ...
        0.001*rew, 0*rew, 'r^', ...         
        0.001*pun, 0*pun, 'ko', 'MarkerFaceColor', [1 0 0]);
    legend('synaptic weight', 'eligibility trace', 'DA', 'ST', 'rew', 'pun');
    grid on
    
    drawnow;
    % ---- end plot ------
    STDP(:,1:D+1)=STDP(:,1001:1001+D);
    ind = find(firings(:,1) > 1001-D);
    firings=[-D 0;firings(ind,1)-1000,firings(ind,2)];
end;
