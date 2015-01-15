helga-quip
======================

"Always with the witty retorts, that one"
-quote that totally happened by a wise and ausipicious gentleman in reference
to helga-quip

Purpose
-------
Match quips and other witticisms. It notes double entendre, hyperbole,
metaphors, and other figures of speech.

Usage
-----
Quip may be used for oneliners or elaborate your mom or thats what she said
jokes. The syntax is:

``!quip add <quip_kind> <quip_regex>``

quip_kind is the kind of quip you'd like to respond with, and can be a templated
response. It could simply be "Your mom" or "That's what she said", but the user
may wish to include the matched regex in the response. This may be done with
{0}, which will be replaced with the matched group.

quip_regex is the searched regular expression to be matched. Any regex should
do, like "that (sounds|is|was) really hard". The search is case insensitive.

Example:
    !quip add "thats what she said" "(it|that|this) (sounds|is|was) really hard"
    <unwitting user>: i took this test last night, and it was really hard
    <bot>: thats what she said
    <unwitting user>: aww bot, your wit knows no bounds! ha ha!

Example2:
    !quip add "your mom {0}" "(looks|is) really (leet|fat|awesome)"
    <unwitting user>: huh this game looks really awesome
    <bot>: your mom looks really awesome
    <unwitting user>: oh bot! you and the jokes, they keep coming so hard!

License
-------

Copyright (c) 2015 Jon Robison

See included LICENSE for licensing information
