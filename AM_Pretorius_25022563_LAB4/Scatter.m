x = linspace(0,3*pi,200);
y = cos(x) + rand(1,200);
%sz = linspace(1,100,200);
scatter(x,y)
title('Received Signal With White Noise')
xlabel('Time (ns)')
ylabel('Signal Amplitude')