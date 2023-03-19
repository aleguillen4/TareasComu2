Ts = 1; %Duracion del simbolo
L = 16; %Muestras por simbolo
a = 0.5; %roll of factor
x = 10;
t = -x:Ts/L:x; %Vector desde -x a x con pasos de Ts/L
%%Function File: h, st = rcosfir(R,nT,rate,T,filterType)
%%
%%    Implements a cosine filter or root cosine filter impulse response
%%
%%    R Roll-off factor
%%
%%    nT scalar vector of length 2 such as N = (nT(2)-nT(1))*rate+1
%%
%%    T symbol rate
%%
%%    filterType ’normal’ or ’sqrt’
%%
%%    h impulse response
%%
%%    st sampling interval
%%
%%    Example:
%% sltmp/AB09JV.f:691:72: note: code may be misoptimized unless ‘-fno-strict-aliasing’ is used
%%    h = rcosfir(0.2,[-3 3],4,1,’sqrt’);
%%
%%    See also: filter, downsample, rectfilt. 
a = [0 0.25 0.5 0.75 1 1.25];
valores = length (a);
%R = a;
%pt = rcosfir(R, [-x x], L, Ts, 'normal')
Legend=cell(valores,1);
iter = 1;
for i = a
  pt = rcosdesign(i, [-x x], L, Ts, 'normal');
  plot(t, pt)
  Legend{iter}=strcat('Pulso con roll0-off: ', num2str(i));
  grid on
  hold on
  iter = iter + 1;
end
plot(Ts,ylim)
legend(Legend)