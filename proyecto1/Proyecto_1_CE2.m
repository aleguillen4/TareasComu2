% PROYECTO 1
% INTEGRANTES
%   VICTOR FERNANDEZ DIAZ

%--------------------------------------------------------------------------
espera = 5; % Tiempo de espera entre graficos
%--------------------------------------------------------------------------

                    % COSENO ALZADO: Distintos alphas

Ts = 1; % Duracion del simbolo
L = 16; % Numero de muestras por simbolo
t = -3:Ts/L:3; % Vector del tiempo para el eje X
% a: Factor de rodamiento

% 1) Generacion de 4 curvas con 4 alphas distintos - Normal
for a = 0:0.25:1
    if a ~= 0.5
        pt = rcosdesign(a,6,L,'normal');
        plot(t, pt)
        
        if a == 1
            hold off
        else
            hold on         
        end
    end
end

% Malla y leyendas
grid on
legend ('Alpha=0', 'Alpha=0.25', 'Alpha=0.75', 'Alpha=1')

% Titulo Ejes
xlabel('Tiempo [Ts]','FontSize',14,'FontWeight','bold');
ylabel('Magnitud','FontSize',14,'FontWeight','bold');

% Titulo Grafico
title('Coseno Alzado Normal: Múltiples factores de rodamiento','FontSize',16,'FontWeight','bold'); 

pause(espera)
clf

% 2) Generacion de 4 curvas con 4 alphas distintos - SQRT
for a = 0:0.25:1
    if a ~= 0.5
        pt = rcosdesign(a,6,L,'sqrt');
        plot(t, pt)
        
        if a == 1
            hold off
        else
            hold on         
        end
    end
end

% Malla y leyendas
grid on
legend ('Alpha=0', 'Alpha=0.25', 'Alpha=0.75', 'Alpha=1')

% Titulo Ejes
xlabel('Tiempo [Ts]','FontSize',14,'FontWeight','bold');
ylabel('Magnitud','FontSize',14,'FontWeight','bold');

% Titulo Grafico
title('Coseno Alzado Raíz Cuadrada (SRRC): Múltiples factores de rodamiento','FontSize',16,'FontWeight','bold'); 

pause(espera)
clf
%--------------------------------------------------------------------------
%--------------------------------------------------------------------------

                    % CONVOLUCION #1: p(t)*x1(t)

t = -5:0.01:5;    % Conjunto de valores para Tiempo(t)

x = zeros(size(t));  
x(round(length(t)/2)) = 1;  % Pulso de Dirac

y = tripuls(t,5);   % Pulso Triangular

z = conv(x,y,'same')*0.01;   % Convolucion de ambas funciones

% Graficacion de ambas funciones y el resultado final
subplot(3,1,1)
plot(t,x)
xlabel('t')
ylabel('\delta(t)')
title('Delta Dirac')

subplot(3,1,2)
plot(t,y)
xlabel('t')
ylabel('tri(t)')
title('Pulso Triangular')

subplot(3,1,3)
plot(t,z)
xlabel('t')
ylabel('Convolucion')
title('Convolucion del delta Dirac y Pulso Triangular')

pause(espera)
clf

%--------------------------------------------------------------------------
%--------------------------------------------------------------------------

                  % CONVOLUCION #2: p(t)*x2(t)

t = -10:0.01:10;    % Conjunto de valores para Tiempo(t)

x = zeros(size(t));  
x(t==7.5) = 1;  % T=2.5, por lo tanto, 3T=7.5

y = tripuls(t,5);   % Pulso Triangular

z = conv(x,y,'same')*0.01;   % Convolucion de ambas funciones

% Graficacion de ambas funciones y el resultado final
subplot(3,1,1)
plot(t,x)
xlabel('t')
ylabel('\delta(t-7.5)')
title('Delta Dirac')

subplot(3,1,2)
plot(t,y)
xlabel('t')
ylabel('tri(t)')
title('Pulso Triangular')

subplot(3,1,3)
plot(t,z)
xlabel('t')
ylabel('Convolucion')
title('Convolucion del delta Dirac y Pulso Triangular')

pause(espera)
clf

%--------------------------------------------------------------------------
%--------------------------------------------------------------------------

                    % CONVOLUCION #3: p(t)*x3(t)

t = -10:0.01:10;    % Conjunto de valores para Tiempo(t)

x = zeros(size(t));  
x(t==0) = 1;  
x(t==7.5) = 1;  % 3T=7.5

y = tripuls(t,5);   % Pulso Triangular

z = conv(x,y,'same')*0.01;   % Convolucion de ambas funciones

% Graficacion de ambas funciones y el resultado final
subplot(3,1,1)
plot(t,x)
xlabel('t')
ylabel('\delta(t) + \delta(t-7.5)')
title('Funciones Delta Dirac')

subplot(3,1,2)
plot(t,y)
xlabel('t')
ylabel('tri(t)')
title('Pulso Triangular')

subplot(3,1,3)
plot(t,z)
xlabel('t')
ylabel('Convolucion')
title('Convolucion del delta Dirac y Pulso Triangular')

pause(espera)
clf

%--------------------------------------------------------------------------
%--------------------------------------------------------------------------
              
                    % CONVOLUCION #4: p(t)*x(t)

t = -10:0.01:10;    % Conjunto de valores para Tiempo(t)

x = zeros(size(t)); 
x(t==0) = 1;  
x(t==2.5) = 1; % T=2.5
x(t==5) = -1;  % 2T=5
x(t==7.5) = 1;  % 3T=7.5

y = tripuls(t,5);   % Pulso Triangular

z = conv(x,y,'same')*0.01;   % Convolucion de ambas funciones

% Graficacion de ambas funciones y el resultado final
subplot(3,1,1)
plot(t,x)
xlabel('t')
ylabel('\delta(t) - \delta(t-2.5) + \delta(t-5) + \delta(t-7.5)')
title('Funciones Delta Dirac')

subplot(3,1,2)
plot(t,y)
xlabel('t')
ylabel('tri(t)')
title('Pulso Triangular')

subplot(3,1,3)
plot(t,z)
xlabel('t')
ylabel('Convolucion')
title('Convolucion del delta Dirac y Pulso Triangular')