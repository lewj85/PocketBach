\version "2.16.0"  % necessary for upgrading to future LilyPond versions.

% in-line comment syntax
%{ multiple line 
comment syntax %}
% note pitches are always lowercase, so "c" but not "C"

\language "english"  % use "f" for flat, "s" for sharp, ff and ss for doubles
% if not "english" then "is" for sharp, "es" for flat, isis and eses for doubles

%{ note durations are: 1=whole note, 2=half note, 4=quarter note, 8, 16...128
so c4 is a quarter note c, gis16 (or gs16 in "english") is a sixteenth note g#
and r instead of pitch is rest, so r1 is a whole note rest, r2 is a half note rest %}

% sample music
\relative c'  % relative mode always moves to closest note starting at the given pitch
{ 
 % if you don't specify \time it defaults to common time "C"
 c4 d e  % the first measure does not need to be filled, they become pick-up notes 
 \time 3/4  % change time signature
 c8 d e f g a
 fff  % white space is irrelevant, can break measures onto different lines
 r8 ess2
 f1 e4 d  % but notice that you can go beyond a measure if you're not careful
 \numericTimeSignature \time 4/4  % to use "4/4" instead of common time "C"
 r4 r2 r4
}



