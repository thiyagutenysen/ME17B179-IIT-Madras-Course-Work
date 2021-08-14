x = (1:7000)*0.0001;
count = zeros(1,7000);
for i=1:7000
    y = question2(x(i));
    [pks,locs] = findpeaks(y, 'MinPeakProminence',5);
    flag=0;
    for k=1:length(pks)
        if pks(k)<10
            flag=1;
        end
    end
    if flag==0
        [pks,locs] = findpeaks(y, 'MinPeakProminence',5);
        if(length(pks)>=2)
            if locs(length(pks))-locs(1)>7000
                time_period = (locs(length(pks))-locs(1))*0.01*0.001;
                time_per_wave = time_period/(length(pks)-1);
                frequency = 1/time_per_wave;
                count(i) = frequency;
            else
                count(i)=length(pks);
            end
        else
            count(i)=length(pks);
        end
    else
        if max(y)>=10
            [pks,locs] = findpeaks(y, 'MinPeakHeight',10);
            count(i)=length(pks);
        else
            count(i)=0;
        end
    end
end

iext = (1:7000)*0.0001;
figure(1)
%subplot(2,1,1)
plot(iext,count, 'LineWidth',2)
title('count vs iext')
xlabel('external current')
ylabel('spikes-frequency')

hold on
indx = find(diff(count)> 0.99999 | diff(count)< -0.99999);
index = [indx(1),indx(5),indx(7)];
scatter(index*0.0001,count(index),50,'LineWidth',2)

hold off

fprintf('i1 = %.4f \n',index(1)*0.0001);
fprintf('i2 = %.4f \n',index(2)*0.0001);
fprintf('i3 = %.4f \n',index(3)*0.0001);
