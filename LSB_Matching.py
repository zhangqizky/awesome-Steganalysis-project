for i=1:100 
    cover=double(imread(['\LSB_Matching\' num2str(i) '.bmp'])); 
    [m n]=size(cover); 
    message=double(rand(m,n)>0.5); 
    message_plus=2*(double(rand(m,n)>0.5)-0.5); 
    cover1=mod(cover,2); 
    a=cover1; 
    for x=1:m 
        for y=1:n
            % if cover(x,y)==0
            % cover(x,y)=cover(x,y)+1;
            % elseif cover(x,y)==255
            % cover(x,y)=cover(x,y)-1; 
            if cover1(x,y)==message(x,y) 
                cover1(x,y)=message(x,y);
            elseif cover1(x,y)==0 
                cover1(x,y)=cover(x,y)+1; 
            elseif cover1(x,y)==255 
                cover1(x,y)=cover(x,y)-1; 
            else cover1(x,y)=cover(x,y)+message_plus(x,y); 
        end 
    end 
end 
cover=cover1+(cover-a); 
test=mod(cover,2); 
length(find((double(test)-message)~=0))
% imwrite(cover,['\LSB_Matching\stego1_' num2str(i) '.bmp']);
end
