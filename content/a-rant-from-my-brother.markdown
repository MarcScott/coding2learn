Title: A rant from my brother
date: 2013-09-26 19:03
slug: a-rant-from-my-brother

My brother is the reason I learned to code. To be honest, he's probably forgotten more about programming than I'll ever know, and I'm not exaggerating. His preferred languages are Haskell and OCaml, but he's recently had to dive into Javascript for a project he's working on. I received this email from him tonight, and I found it amusing so I thought I'd share it. (Note - he talks about Python a lot as it's the language I understand the most.)

Javascript is pretty pathetic when it comes to bug-finding. Here's some Python:

	>>> foo = {}
	>>> foo["bar"] = 3
	>>> foo["baz"]

The dictionary foo doesn't have a key "baz", and this is likely a typo. Python sensibly throws an error, and execution will not continue.

In Javascript:

	>> var foo = {};
	>> foo["bar"] = 3;
	>> foo["baz"]

This does not throw any errors, but instead returns undefined. This is not entirely retarded, until we find that Javascript happily coerces undefined to NaN (Not a Number) whenever it appears in arithmetic expressions. Since NaN is a valid floating point number, it can happily propagate through running code. Things go from entirely retarded to completely fucking braindead when we find that Javascript will accept NaN as an argument in most functions:

	ctx.fillRect(NaN,NaN,NaN,NaN)

In other words, what started out as a typo which would have Python raise an error at the earliest possible opportunity is silently ignored by Javascript, only to be found if one notices certain rectangles not being drawn. Tracking down such a typo from a bit of missing graphics is going to be a pain in the arse.

Now functions: Javascript has no time for conventions of mathematics, programming, or basic sanity. In Javascript, any function can be passed *any* number of arguments without raising an error. The concept of arity be damned. Extra arguments in Javascript are ignored. Missing arguments are set to undefined. And, as explained before, undefined will be coerced to NaN in arithmetic expressions to create lots of great bug-full code when you forget the number of arguments required of a function. For further hilarity, undefined can be used as a key to a dictionary. So if you do:

	function insert(y,x) {
	   dict[x] = y;
	   ...
	}

and you accidentally call insert(3), you won't be told, as you would be in Python, that you are missing a required argument. Instead, x gets bound to undefined, and the dictionary will be become

	{ undefined : 3 }

That's almost certainly an unexpected behaviour.

The way that function parameters are interpreted leads to this truly bizarre example, which I got from another site:

	['10','10','10','10','10'].map(parseInt)

this yields the truly *weird*

	[10,NaN,2,3,4]

The function *map* is supposed to apply its argument to every value in a list. In sane languages, 

	[x,x,x,x,x].map(f) 

should give you the list

	[f(x),f(x),f(x),f(x),f(x)]

In Javascript, for likely dumbfuck reasons, map takes a function of three arguments. The first argument is bound to the element in the list. The second argument is bound to the index into the list. The third argument is bound to the entire list. This will cause surprise when you don't know exactly how many arguments the argument to map is expecting (parseInt in this case), but don't expect a prompt error in case of mistakes, as you would get in Python.

It turns out that, in this case, parseInt takes an optional second argument which is the base in which the first argument is to be interpreted. For unexplored reasons, when the base is 0, the argument is read in base 10. In base 1, NaN is always returned. This explains the first two elements in

	[10,NaN,2,3,4]

The third element is "10" in base 2. The fourth element is "10" in base 3. The last element is 10 in base 4

Ridiculous.