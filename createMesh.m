function [X,Y,Z] = createMesh(initial,final,space)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
x = initial:space:final;
y = initial:space:final;
[X,Y] = meshgrid(x,y);
Z = sin(X)+cos(Y);
% s = surf(X,Y,Z);
% ax = gca;
% fig = figure;
end