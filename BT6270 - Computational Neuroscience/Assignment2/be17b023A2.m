% BT6270 Neuroscience
% Code by: Nivethithan M
% 22-10-2020

% Parameters
a = 0.5;
r = 0.1;
b = 0.1;
Iext = 0.8;
v0 = 0.8;
w0 = 0.8;

% Code here-->
tinit=0; %initial time
tfin=100; %final time
h = 1; % time step
nsteps = (tfin-tinit)/h + 1;  % this is the number of elements in t(a:h:b) (It is = N+1)
v=zeros(1,nsteps);
w=zeros(1,nsteps);
t=tinit:h:tfin;
dvdt = @(v,w,t) (-v^3 + (a+1)*v^2 - a*v - w + Iext); 
dwdt = @(v,w,t) (b*v - w*r);
v(1) = v0;
w(1) = w0;
for n=1:nsteps
    v(n+1)=v(n)+h.*dvdt(v(n),w(n),t(n));
    w(n+1)=w(n)+h.*dwdt(v(n),w(n),t(n)); 
    t(n+1)=tinit+n*h;
end

% Plots
figure
subplot(1,1,1)
plot(t,v,'-',t,w,'--')
legend('v','w')

hold on
