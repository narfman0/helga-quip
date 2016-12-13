helga-quip
======================

.. image:: https://badge.fury.io/py/helga-quip.png
    :target: https://badge.fury.io/py/helga-quip

.. image:: https://travis-ci.org/narfman0/helga-quip.png?branch=master
    :target: https://travis-ci.org/narfman0/helga-quip

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

``!quip add <quip_regex> <quip_kind>``

quip_kind is the kind of quip you'd like to respond with, and can be a templated
response. It could simply be "Your mom" or "That's what she said", but the user
may wish to include the matched regex in the response. This may be done with
{0}, which will be replaced with the matched group. Other positionals may be
used, or named groups are supported now similar to (?P<name>expression).

quip_regex is the searched regular expression to be matched. Any regex should
do, like "that (sounds|is|was) really hard". The search is case insensitive.
If there are multiple matches, a random response will be selected.

Example::

    !quip add "(it|that|this) (sounds|is|was) really hard" "thats what she said"
    <unwitting user>: i took this test last night, and it was really hard
    <bot>: thats what she said
    <unwitting user>: aww bot, your wit knows no bounds! ha ha!

Example2::

    !quip add "(looks|is) really (leet|fat|awesome)" "your mom {0} really {1}"
    <irc noob>: huh this game looks really awesome
    <bot>: your mom looks really awesome
    <irc noob>: oh bot! you and the jokes, they keep coming so hard!

Example3 (named backreferences)::

    !quip add "(?:(?:i|he|you) (?:is|am)) (?P<action>excited|giddy)" "your mom is {action}"
    <foolish scrub>: man, i am excited for the concert!
    <bot>: your mom is excited
    <foolish scrub>: YOUR MOM IS...
    <foolish scrub> has left the chat

Example4 (positonals)::

    !quip add "[am|is] (lord|king) of (me|him|her|she|he)" "your mom is {0} of {1}"
    <naive user>: ...man, i am lord of him! shot right in the face, and he wasn't doing nothin'!
    <bot>: your mom is lord of him
    <naive user> sobs at the truth of it all

``!quip dump``

Dumps to the paste service dpaste with entries of '"regex" "kind"'

License
-------

Copyright (c) 2016 Jon Robison

See included LICENSE for licensing information
