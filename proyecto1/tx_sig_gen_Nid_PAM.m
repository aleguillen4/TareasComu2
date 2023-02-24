%tx_sig_gen.m
clear all;
close all;

rand(1,1256);  % Ultimos 3 digitos del carnet: 256.

Ts = 1;
L  = 16;
alpha = 0.25; %Roll-off solicitado
t_step = Ts/L;

%%%%%%%%%<1. Generacion de onda del pulso > %%%%%%%%%%%%%%%%%%%%%%
pt = rcosdesign(alpha,6,L,'normal');
pt = pt/(max(abs(pt))); %rescaling to match rcosine

%%%%%%%%%<2. Generacion de 100 simbolos binarios >%%%%%%%%%%%%%%%%%%%%
Ns = 100;
data_bit = (rand(1,Ns)>0.5);

%%%%%%%%%<3. Unipolar a Bipolar (modulacion de amplitud)>%%%%%%%%%%%%%%
amp_modulated = 2*ceil(rand(1,Ns)*4)-5;

%%%%%%%%%<4.  Modulacion de pulsos >%%%%%%%%%%%%%%%%%%%%%%%%%%%%
impulse_modulated = [];
for n=1:Ns
    delta_signal = [amp_modulated(n)  zeros(1, L-1)];
    impulse_modulated = [impulse_modulated  delta_signal];
end

%%%%%%%%<5.Formacion de pulsos (filtrado de transmision)>%%%%%%%%%%
tx_signal = conv(impulse_modulated, pt);

%%%%%%%%<6.Graficacion>%%%%%%%%%%
figure(100)
subplot(2,1,1)
stem(t_step:t_step:(Ns*Ts), impulse_modulated, '. ');
axis([0 Ns*Ts -2*max(impulse_modulated) 2*max(impulse_modulated) ]);
grid on
title('impulse modulated')
subplot(2,1,2)
plot(t_step:t_step:(t_step*length(tx_signal)), tx_signal);
axis([0 Ns*Ts -2*max(tx_signal) 2*max(tx_signal)]);
grid on
title('pulse shaped')


figure(200)
for k=3: floor(Ns/2)-1 % k representa la k-esima muestra
tmp = tx_signal(((k-1)*2*L+1):(k*2*L));
plot(t_step*(0:(2*L-1)), tmp);
axis([0 2 min(tx_signal) max(tx_signal)]);
grid on;
hold on
%pause
end

hold off

