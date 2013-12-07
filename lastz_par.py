#! /usr/bin/python

#one more line
import argparse, os
from multiprocessing import Pool

def list_maker(ref_list, query_list, parameters):
	list1 = []
	for ref in ref_list:
		for query in query_list:
			#a = 'lastz ri qi M=254 O=600 E=150 K=4500 Y=15000 T=2 > lav/ri-qi.lav' 
			out_file_name =  ref.strip('.nib\n').split('/')[-1] + '-' + query.strip('.nib\n').split('/')[-1]
			a = 'lastz %s %s %s > lav/%s.lav' % (ref.strip('\n'), query.strip('\n'), parameters, out_file_name)
			list1.append(a)
	return list1


parser = argparse.ArgumentParser()
parser.add_argument('-N', help="Number of cores", type=int, default=6)
parser.add_argument('-ref', help="File with reference list", type=str, default='ref_list1.txt')
parser.add_argument('-que', help="File with rquery list", type=str, default='query_list.txt')
parser.add_argument('-M', help="parameter for LASTZ", type=int, default=254)
parser.add_argument('-O', help="parameter for LASTZ", type=int, default=600)
parser.add_argument('-E', help="parameter for LASTZ", type=int, default=150)
parser.add_argument('-K', help="parameter for LASTZ", type=int, default=4500)
parser.add_argument('-Y', help="parameter for LASTZ", type=int, default=15000)
parser.add_argument('-T', help="parameter for LASTZ", type=int, default=2)

args = parser.parse_args()

p = Pool(processes = args.N)

ref_list_file_name = args.ref
query_list_file_name = args.que

ref_list_file = open(ref_list_file_name, 'r')
query_list_file = open(query_list_file_name, 'r')

ref_list = ref_list_file.readlines()
query_list = query_list_file.readlines()

ref_list_file.close()
query_list_file.close()

parameters = 'M=%d O=%d E=%d K=%d Y=%d T=%d' % (args.M, args.O, args.E, args.K, args.Y, args.T)

list1 = list_maker(ref_list, query_list, parameters)

p.map(os.system, list1)		

#for i in list1: print i
