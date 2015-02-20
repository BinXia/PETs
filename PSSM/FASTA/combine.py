import os


combination = open('./Dset186.fasta', 'w');
for proteinFile in os.listdir('./Dset186/'):
	if proteinFile[0] == '.':
		continue;
	with open('./Dset186/%s'%proteinFile) as datum:
		data = datum.readlines();

	for ln,datum in enumerate(data):
		datum = datum.strip();
		if ln == 0:
			datum = datum.split('|')[0];
			combination.write('\n{0}\n'.format(datum[0:5]+datum[6:]));
		elif datum == []:
			continue;
		else:
			combination.write('{0}'.format(datum));


combination.close();